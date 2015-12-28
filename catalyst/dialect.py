from sqlalchemy.engine.default import DefaultDialect
from sqlalchemy import exc

import os

from . import json_dbapi


class JsonDialect(DefaultDialect):
    def __init__(self, **kwargs):
        super(JsonDialect, self).__init__(**kwargs)

    @classmethod
    def dbapi(cls):
        return json_dbapi

    name = 'json'
    supports_alter = False
    supports_unicode_statements = True
    supports_unicode_binds = True
    supports_default_values = True
    supports_empty_insert = False
    supports_cast = True
    supports_multivalues_insert = True
    supports_right_nested_joins = False

    def create_connect_args(self, url):
        if url.username or url.password or url.host or url.port:
            raise exc.ArgumentError(
                "Invalid JsonDB URL: %s\n"
                "Valid JsonDB URL forms are:\n"
                " json:///relative/path/to/file.json\n"
                " json:////absolute/path/to/file.json" % (url,))
        filename = os.path.abspath(url.database)

        opts = url.query.copy()
        return [filename], opts

    default_paramstyle = 'format'
    # execution_ctx_cls = SQLiteExecutionContext
    # statement_compiler = SQLiteCompiler
    # ddl_compiler = SQLiteDDLCompiler
    # type_compiler = SQLiteTypeCompiler
    # preparer = SQLiteIdentifierPreparer
    # ischema_names = ischema_names
    # colspecs = colspecs
    # isolation_level = None
    #
    # supports_cast = True
    # supports_default_values = True
    #
    # construct_arguments = [
    #     (sa_schema.Table, {
    #         "autoincrement": False
    #     }),
    #     (sa_schema.Index, {
    #         "where": None,
    #     }),
    # ]


