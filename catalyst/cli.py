import os
import os.path
import argparse
import json
import importlib
import sys

from . import utils

from .schema import dump_metadata, load_metadata


def init(args):
    if os.path.isfile("catalyst.json"):
        raise Exception("Config file 'catalyst.json' already exists")

    if os.path.isdir(args.folder):
        raise Exception("Migrations folder '%s' already exists" % args.folder)

    with utils.status("Creating migrations folder '%s'" % args.folder):
        os.mkdir(args.folder)

    config = {
        'folder': args.folder,
        'metadata': 'module:metadata'
    }

    with utils.status("Creating config file 'catalyst.json'"):
        with open("catalyst.json", "w") as f:
            json.dump(config, f, indent=2)


def save(args):
    with utils.status("Reading config file 'catalyst.json'"):
        with open("catalyst.json", "r") as f:
            config = json.load(f)

    metadata = config['metadata']
    module_name, variable_name = metadata.split(":")

    sys.path.insert(0, '')
    metadata = importlib.import_module(module_name)
    for variable_name in variable_name.split("."):
        metadata = getattr(metadata, variable_name)

    info = dump_metadata(metadata)

    print(json.dumps(info, indent=2))

    from .utils import info_hash
    print(info_hash(info))


def migrate(args):
    with utils.status("Reading config file 'catalyst.json'"):
        with open("catalyst.json", "r") as f:
            config = json.load(f)

    metadata = config['metadata']
    module_name, variable_name = metadata.split(":")

    sys.path.insert(0, '')
    metadata = importlib.import_module(module_name)
    for variable_name in variable_name.split("."):
        metadata = getattr(metadata, variable_name)

    from sqlalchemy import create_engine, MetaData, select

    assert args.data != args.target

    src_engine = create_engine(args.data)
    dst_engine = create_engine(args.target)

    # clear out any existing tables
    dst_metadata = MetaData(bind=dst_engine)
    dst_metadata.reflect()
    dst_metadata.drop_all()

    # create new tables
    dst_metadata = metadata
    dst_metadata.create_all(dst_engine)

    # import data
    with dst_engine.connect() as dst_conn:
        src_metadata = MetaData(bind=src_engine)
        src_metadata.reflect()
        for dst_table in dst_metadata.sorted_tables:
            if dst_table.name in src_metadata.tables:
                with utils.status("Migrating table '%s'" % dst_table.name):
                    src_table = src_metadata.tables[dst_table.name]
                    common_cols = list(set(
                        column.name for column in dst_table.columns
                    ).intersection(set(
                        column.name for column in src_table.columns
                    )))
                    select_query = select([src_table.columns[name] for name in common_cols])
                    insert_query = dst_table.insert().compile(bind=dst_engine, column_keys=common_cols)
                    data = list(select_query.execute())
                    dst_conn.execute(insert_query, data)

def dbinit(args):
    from sqlalchemy import create_engine
    engine = create_engine(args.uri)

    with utils.status("Reading config file 'catalyst.json'"):
        with open("catalyst.json", "r") as f:
            config = json.load(f)

    metadata = config['metadata']
    module_name, variable_name = metadata.split(":")

    sys.path.insert(0, '')
    metadata = importlib.import_module(module_name)
    for variable_name in variable_name.split("."):
        metadata = getattr(metadata, variable_name)

    info = dump_metadata(metadata)

    metadata = load_metadata(info)


def main():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest='command')
    commands.required = True

    # Init
    cmd = commands.add_parser('init', help="Initialize the catalyst environment")
    cmd.set_defaults(func=init)
    cmd.add_argument('folder', type=str)

    # Create
    cmd = commands.add_parser('dbinit', help="Initialize a new DB")
    cmd.set_defaults(func=dbinit)
    cmd.add_argument('uri', type=str)

    # Revision
    cmd = commands.add_parser('save', help="Save current metadata")
    cmd.set_defaults(func=save)

    # Migrate
    cmd = commands.add_parser('migrate', help="Migrate a DB")
    cmd.add_argument('data', type=str)
    cmd.add_argument('target', type=str)
    cmd.set_defaults(func=migrate)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
