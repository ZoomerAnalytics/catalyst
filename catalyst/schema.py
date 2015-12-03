from sqlalchemy import MetaData, Table, Column

from sqlalchemy import PrimaryKeyConstraint, CheckConstraint, ForeignKeyConstraint

from sqlalchemy.sql.sqltypes import *

import json


def load_column(info):
    info["type_"] = eval(info["type_"])
    return Column(**info)


def dump_column(column):
    info = {
        "name": column.name,
        "type_": repr(column.type),
        "nullable": column.nullable
    }
    if column.primary_key:
        info["autoincrement"] = True
    if column.default is not None:
        info["default"] = column.default.arg
    if not column.autoincrement:
        info["autoincrement"] = False
    return info


def load_constraint(info):
    if "foreign_key" in info:
        info = info['foreign_key']
        return ForeignKeyConstraint(
            info['columns'],
            [
                "%s.%s" % (info['parent']['table'], pcolumn)
                for pcolumn in info['parent']['columns']
            ]
        )
    else:
        raise ValueError("Could not load constraint")


def dump_constraint(constraint):
    if isinstance(constraint, ForeignKeyConstraint):
        info = {
            'columns': [
                column.name
                for column in constraint.columns
            ],
            'parent': {
                "table": constraint.referred_table.name,
                "columns": [
                    element.column.name
                    for element in constraint.elements
                ]
            }
        }
        info = {'foreign_key': info}
    elif isinstance(constraint, CheckConstraint):
        # copied from alembic
        # detect the constraint being part of
        # a parent type which is probably in the Table already.
        # ideally SQLAlchemy would give us more of a first class
        # way to detect this.
        if (
            constraint._create_rule
            and hasattr(constraint._create_rule, 'target')
            and isinstance(constraint._create_rule.target, TypeEngine)
        ):
            return None
        raise NotImplementedError("Unsupported constraint <%s>" % type(constraint))
    elif isinstance(constraint, PrimaryKeyConstraint):
        # dealt with during column setup
        return None
    else:
        raise NotImplementedError("Unsupported constraint <%s>" % type(constraint))
    return info


def load_table(info, metadata):
    return Table(
        info['name'],
        metadata
        *([
            load_column(column_info)
            for column_info in info['columns']
        ]+[
            load_constraint(constraint_info)
            for constraint_info in info['constraints']
        ])
    )


def dump_table(table):
    constraints = []
    for constraint in table.constraints:
        info = dump_constraint(constraint)
        if info is not None:
            constraints.append(info)

    return {
        "columns": [
            dump_column(column)
            for column in table.columns
        ],
        "constraints": constraints
    }


def load_metadata(info):
    metadata = MetaData()
    for table_info in info['tables']:
        load_table(table_info, metadata)
    return metadata


def dump_metadata(metadata):
    return {
        "tables": {
            table_name: dump_table(table)
            for table_name, table in metadata.tables.items()
        }
    }