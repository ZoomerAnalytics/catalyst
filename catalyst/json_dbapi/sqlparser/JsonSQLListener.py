# Generated from JsonSQL.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JsonSQLParser import JsonSQLParser
else:
    from JsonSQLParser import JsonSQLParser

# This class defines a complete listener for a parse tree produced by JsonSQLParser.
class JsonSQLListener(ParseTreeListener):

    # Enter a parse tree produced by JsonSQLParser#select_stmt.
    def enterSelect_stmt(self, ctx:JsonSQLParser.Select_stmtContext):
        pass

    # Exit a parse tree produced by JsonSQLParser#select_stmt.
    def exitSelect_stmt(self, ctx:JsonSQLParser.Select_stmtContext):
        pass


    # Enter a parse tree produced by JsonSQLParser#select_core.
    def enterSelect_core(self, ctx:JsonSQLParser.Select_coreContext):
        pass

    # Exit a parse tree produced by JsonSQLParser#select_core.
    def exitSelect_core(self, ctx:JsonSQLParser.Select_coreContext):
        pass


    # Enter a parse tree produced by JsonSQLParser#from_clause.
    def enterFrom_clause(self, ctx:JsonSQLParser.From_clauseContext):
        pass

    # Exit a parse tree produced by JsonSQLParser#from_clause.
    def exitFrom_clause(self, ctx:JsonSQLParser.From_clauseContext):
        pass


    # Enter a parse tree produced by JsonSQLParser#table_or_subquery.
    def enterTable_or_subquery(self, ctx:JsonSQLParser.Table_or_subqueryContext):
        pass

    # Exit a parse tree produced by JsonSQLParser#table_or_subquery.
    def exitTable_or_subquery(self, ctx:JsonSQLParser.Table_or_subqueryContext):
        pass


    # Enter a parse tree produced by JsonSQLParser#table_name.
    def enterTable_name(self, ctx:JsonSQLParser.Table_nameContext):
        pass

    # Exit a parse tree produced by JsonSQLParser#table_name.
    def exitTable_name(self, ctx:JsonSQLParser.Table_nameContext):
        pass


    # Enter a parse tree produced by JsonSQLParser#result_column.
    def enterResult_column(self, ctx:JsonSQLParser.Result_columnContext):
        pass

    # Exit a parse tree produced by JsonSQLParser#result_column.
    def exitResult_column(self, ctx:JsonSQLParser.Result_columnContext):
        pass


    # Enter a parse tree produced by JsonSQLParser#unary_expr.
    def enterUnary_expr(self, ctx:JsonSQLParser.Unary_exprContext):
        pass

    # Exit a parse tree produced by JsonSQLParser#unary_expr.
    def exitUnary_expr(self, ctx:JsonSQLParser.Unary_exprContext):
        pass


    # Enter a parse tree produced by JsonSQLParser#expr.
    def enterExpr(self, ctx:JsonSQLParser.ExprContext):
        pass

    # Exit a parse tree produced by JsonSQLParser#expr.
    def exitExpr(self, ctx:JsonSQLParser.ExprContext):
        pass


    # Enter a parse tree produced by JsonSQLParser#signed_number.
    def enterSigned_number(self, ctx:JsonSQLParser.Signed_numberContext):
        pass

    # Exit a parse tree produced by JsonSQLParser#signed_number.
    def exitSigned_number(self, ctx:JsonSQLParser.Signed_numberContext):
        pass


    # Enter a parse tree produced by JsonSQLParser#literal_value.
    def enterLiteral_value(self, ctx:JsonSQLParser.Literal_valueContext):
        pass

    # Exit a parse tree produced by JsonSQLParser#literal_value.
    def exitLiteral_value(self, ctx:JsonSQLParser.Literal_valueContext):
        pass


