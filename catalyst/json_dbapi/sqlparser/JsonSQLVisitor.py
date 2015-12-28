# Generated from JsonSQL.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JsonSQLParser import JsonSQLParser
else:
    from JsonSQLParser import JsonSQLParser

# This class defines a complete generic visitor for a parse tree produced by JsonSQLParser.

class JsonSQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JsonSQLParser#select_stmt.
    def visitSelect_stmt(self, ctx:JsonSQLParser.Select_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonSQLParser#select_core.
    def visitSelect_core(self, ctx:JsonSQLParser.Select_coreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonSQLParser#from_clause.
    def visitFrom_clause(self, ctx:JsonSQLParser.From_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonSQLParser#table_or_subquery.
    def visitTable_or_subquery(self, ctx:JsonSQLParser.Table_or_subqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonSQLParser#table_name.
    def visitTable_name(self, ctx:JsonSQLParser.Table_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonSQLParser#result_column.
    def visitResult_column(self, ctx:JsonSQLParser.Result_columnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonSQLParser#unary_expr.
    def visitUnary_expr(self, ctx:JsonSQLParser.Unary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonSQLParser#expr.
    def visitExpr(self, ctx:JsonSQLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonSQLParser#signed_number.
    def visitSigned_number(self, ctx:JsonSQLParser.Signed_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonSQLParser#literal_value.
    def visitLiteral_value(self, ctx:JsonSQLParser.Literal_valueContext):
        return self.visitChildren(ctx)



del JsonSQLParser