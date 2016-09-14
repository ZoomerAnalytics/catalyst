import os
import os.path
import argparse
import json
import importlib
import sys

from catalyst import utils

from catalyst.schema import dump_metadata, load_metadata


def init(args):
    if os.path.isfile("catalyst.json"):
        raise Exception("Config file 'catalyst.json' already exists")

    # if os.path.isdir(args.folder):
    #     raise Exception("Migrations folder '%s' already exists" % args.folder)
    #
    # with utils.status("Creating migrations folder '%s'" % args.folder):
    #     os.mkdir(args.folder)

    config = {
        'default': {
            'metadata': 'database_package.models_module:Model.metadata',
            'dburi': 'sqlite:///app.db',
            'dumpfile': 'data.json',
        }
    }

    with utils.status("Creating config file 'catalyst.json'"):
        with open("catalyst.json", "w") as f:
            json.dump(config, f, indent=2)


def load_config(label):
    with utils.status("Reading config file 'catalyst.json'"):
        with open("catalyst.json", "r") as f:
            j = json.load(f)
            config = {}
            while label:
                base_config = j.get(label, None)
                if base_config is None:
                    raise Exception("No such config '%s'" % label)
                label = base_config.get('extends', None)
                base_config.update(config)
                config = base_config
            return config


def save(args):
    config = load_config(args.config)

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


def dump(args):
    from sqlalchemy import create_engine, MetaData, select
    from collections import OrderedDict
    from . import xjson

    config = load_config(args.config)

    target = config.get('dumpfile', None)
    if target is None:
        raise Exception("No 'target' argument specified and no 'dumpfile' setting in config file.")

    data = config.get('dburi', None)
    if data is None:
        raise Exception("No 'data' argument specified and no 'dburi' setting in config file.")

    if target == data:
        raise Exception("Data source and target are the same")

    if not args.yes and 'y' != input("Warning: any existing data at '%s' will be erased. Proceed? [y/n]" % target):
        return

    #assert data != target
    #assert "://" not in target

    src_engine = create_engine(data)

    # dump data
    with open(target, "w") as f:
        tables = OrderedDict()
        src_metadata = MetaData(bind=src_engine)
        src_metadata.reflect()
        for src_table in src_metadata.sorted_tables:
            with utils.status("Dumping table '%s'" % src_table.name):
                columns = [column.name for column in src_table.columns]
                select_query = select([src_table.columns[name] for name in columns])
                rows = [
                    list(row)
                    for row in select_query.execute()
                ]
                table = OrderedDict()
                table['columns'] = columns
                table['rows'] = rows
                tables[src_table.name] = table
        xjson.dump(tables, f)


def migrate(args):
    config = load_config(args.config)

    metadata = config['metadata']
    module_name, variable_name = metadata.split(":")

    sys.path.insert(0, '')
    metadata = importlib.import_module(module_name)
    for variable_name in variable_name.split("."):
        metadata = getattr(metadata, variable_name)

    from sqlalchemy import create_engine, MetaData, select

    target = config.get('dburi', None)
    if target is None:
        raise Exception("No 'target' argument specified and no 'dburi' setting in config file.")

    data = config.get('dumpfile', None)
    if data is None:
        raise Exception("No 'data' argument specified and no 'dumpfile' setting in config file.")

    if target == data:
        raise Exception("Data source and target are the same")

    if not args.yes and 'y' != input("Warning: any existing data at '%s' will be erased. Proceed? [y/n]" % target):
        return

    dst_engine = create_engine(target)

    # clear out any existing tables
    dst_metadata = MetaData(bind=dst_engine)
    dst_metadata.reflect()
    dst_metadata.drop_all()

    # create new tables
    dst_metadata = metadata
    dst_metadata.create_all(dst_engine)

    # load source
    from .data import JSONDataSource, SQLADataSource
    if "://" in data:
        src = SQLADataSource(data)
    else:
        src = JSONDataSource(data)

    # import data
    with dst_engine.connect() as dst_conn:
        for dst_table in dst_metadata.sorted_tables:
            if src.has_table(dst_table.name):
                with utils.status("Migrating table '%s'" % dst_table.name):
                    src_cols = src.get_column_names(dst_table.name)
                    common_cols = [
                        column.name
                        for column in dst_table.columns
                        if column.name in src_cols
                    ]
                    data = src.get_data(dst_table.name, common_cols)
                    if data:  # sql complains otherwise
                        insert_query = dst_table.insert().compile(bind=dst_engine, column_keys=common_cols)
                        dst_conn.execute(insert_query, data)


def dbinit(args):
    config = load_config(args.config)

    metadata = config['metadata']
    module_name, variable_name = metadata.split(":")

    sys.path.insert(0, '')
    metadata = importlib.import_module(module_name)
    for variable_name in variable_name.split("."):
        metadata = getattr(metadata, variable_name)

    from sqlalchemy import create_engine, MetaData

    target = config.get('dburi', None)
    if target is None:
        raise Exception("No 'target' argument specified and no 'dburi' setting in config file.")

    if not args.yes and 'y' != input("Warning: any existing data at '%s' will be erased. Proceed? [y/n]" % target):
        return

    dst_engine = create_engine(target)

    # clear out any existing tables
    dst_metadata = MetaData(bind=dst_engine)
    dst_metadata.reflect()
    dst_metadata.drop_all()

    # create new tables
    dst_metadata = metadata
    dst_metadata.create_all(dst_engine)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--yes', '-y', action='store_true', default=False)
    commands = parser.add_subparsers(dest='command')
    commands.required = True

    # Init
    cmd = commands.add_parser('init', help="Initialize the catalyst environment")
    cmd.set_defaults(func=init)

    # Create
    cmd = commands.add_parser('dbinit', help="Initialize a new DB")
    cmd.set_defaults(func=dbinit)
    cmd.add_argument('config', type=str)

    # Revision
    cmd = commands.add_parser('save', help="Save current metadata")
    cmd.set_defaults(func=save)
    cmd.add_argument('config', type=str)

    # Dump
    cmd = commands.add_parser('dump', help="Dump data from DB to JSON file")
    cmd.set_defaults(func=dump)
    cmd.add_argument('config', type=str)

    # Migrate
    cmd = commands.add_parser('migrate', help="Migrate a DB")
    cmd.set_defaults(func=migrate)
    cmd.add_argument('config', type=str)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
