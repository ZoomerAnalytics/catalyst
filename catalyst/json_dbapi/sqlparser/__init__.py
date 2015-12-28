from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.tree.Trees import Trees

from .SQLiteLexer import SQLiteLexer
from .SQLiteParser import SQLiteParser
from .SQLiteListener import SQLiteListener
from .SQLiteVisitor import SQLiteVisitor


class StatementExecutor(object):
    def __init__(self, db):
        self.db = db


class ParsedStatement(object):
    def __init__(self, statement):
        input = InputStream(statement)
        lexer = SQLiteLexer(input)
        stream = CommonTokenStream(lexer)
        parser = SQLiteParser(stream)
        self.tree = parser.sql_stmt()

    def execute(self, db):
        return StatementExecutor(db).execute(self.tree)


def parse(statement):
    return ParsedStatement(statement)