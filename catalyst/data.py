from sqlalchemy import create_engine, MetaData, select

from . import xjson
import six


class SQLADataSource(object):
    def __init__(self, uri):
        self.engine = create_engine(uri)
        self.metadata = MetaData(bind=self.engine)
        self.metadata.reflect()

    def has_table(self, table_name):
        return table_name in self.metadata.tables

    def get_column_names(self, table_name):
        return [
            column.name
            for column in self.metadata.tables[table_name].columns
        ]

    def get_data(self, table_name, columns):
        select_query = select([self.metadata.tables[table_name].columns[name] for name in columns])
        return list(map(list, select_query.execute()))


class JSONDataSource(object):
    def __init__(self, f):
        if isinstance(f, six.string_types):
            with open(f, "r") as f:
                self.json = xjson.load(f)
        else:
            self.json = xjson.load(f)

    def has_table(self, table_name):
        return table_name in self.json

    def get_column_names(self, table_name):
        return self.json[table_name]['columns']

    def get_data(self, table_name, columns):
        src_cols = self.json[table_name]['columns']
        indices = [
            src_cols.index(column)
            for column in columns
        ]
        return [
            {
                src_cols[index]: row[index]
                for index in indices
            }
            for row in self.json[table_name]['rows']
        ]

