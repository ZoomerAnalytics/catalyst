# Generated from JsonSQL.g4 by ANTLR 4.5.1
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\u009f")
        buf.write("K\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\7\3\35\n\3\f\3\16\3 \13\3\3\3\5\3#\n\3\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\5\t\64")
        buf.write("\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t?\n\t\f\t")
        buf.write("\16\tB\13\t\3\n\5\nE\n\n\3\n\3\n\3\13\3\13\3\13\2\3\20")
        buf.write("\f\2\4\6\b\n\f\16\20\22\24\2\7\4\2\n\fhh\3\2\n\13\3\2")
        buf.write("\20\23\3\2\24\27\6\2\668jj\u0098\u0098\u009a\u009bG\2")
        buf.write("\26\3\2\2\2\4\30\3\2\2\2\6$\3\2\2\2\b\'\3\2\2\2\n)\3\2")
        buf.write("\2\2\f+\3\2\2\2\16-\3\2\2\2\20\63\3\2\2\2\22D\3\2\2\2")
        buf.write("\24H\3\2\2\2\26\27\5\4\3\2\27\3\3\2\2\2\30\31\7\u0082")
        buf.write("\2\2\31\36\5\f\7\2\32\33\7\7\2\2\33\35\5\f\7\2\34\32\3")
        buf.write("\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37\"\3")
        buf.write("\2\2\2 \36\3\2\2\2!#\5\6\4\2\"!\3\2\2\2\"#\3\2\2\2#\5")
        buf.write("\3\2\2\2$%\7M\2\2%&\5\b\5\2&\7\3\2\2\2\'(\5\n\6\2(\t\3")
        buf.write("\2\2\2)*\7\u0097\2\2*\13\3\2\2\2+,\5\20\t\2,\r\3\2\2\2")
        buf.write("-.\t\2\2\2./\5\20\t\2/\17\3\2\2\2\60\61\b\t\1\2\61\64")
        buf.write("\5\24\13\2\62\64\5\16\b\2\63\60\3\2\2\2\63\62\3\2\2\2")
        buf.write("\64@\3\2\2\2\65\66\f\5\2\2\66\67\t\3\2\2\67?\5\20\t\6")
        buf.write("89\f\4\2\29:\t\4\2\2:?\5\20\t\5;<\f\3\2\2<=\t\5\2\2=?")
        buf.write("\5\20\t\4>\65\3\2\2\2>8\3\2\2\2>;\3\2\2\2?B\3\2\2\2@>")
        buf.write("\3\2\2\2@A\3\2\2\2A\21\3\2\2\2B@\3\2\2\2CE\t\3\2\2DC\3")
        buf.write("\2\2\2DE\3\2\2\2EF\3\2\2\2FG\7\u0098\2\2G\23\3\2\2\2H")
        buf.write("I\t\6\2\2I\25\3\2\2\2\b\36\"\63>@D")
        return buf.getvalue()


class JsonSQLParser ( Parser ):

    grammarFileName = "JsonSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'.'", "'('", "')'", "','", "'='", 
                     "'*'", "'+'", "'-'", "'~'", "'||'", "'/'", "'%'", "'<<'", 
                     "'>>'", "'&'", "'|'", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'!='", "'<>'" ]

    symbolicNames = [ "<INVALID>", "SCOL", "DOT", "OPEN_PAR", "CLOSE_PAR", 
                      "COMMA", "ASSIGN", "STAR", "PLUS", "MINUS", "TILDE", 
                      "PIPE2", "DIV", "MOD", "LT2", "GT2", "AMP", "PIPE", 
                      "LT", "LT_EQ", "GT", "GT_EQ", "EQ", "NOT_EQ1", "NOT_EQ2", 
                      "K_ABORT", "K_ACTION", "K_ADD", "K_AFTER", "K_ALL", 
                      "K_ALTER", "K_ANALYZE", "K_AND", "K_AS", "K_ASC", 
                      "K_ATTACH", "K_AUTOINCREMENT", "K_BEFORE", "K_BEGIN", 
                      "K_BETWEEN", "K_BY", "K_CASCADE", "K_CASE", "K_CAST", 
                      "K_CHECK", "K_COLLATE", "K_COLUMN", "K_COMMIT", "K_CONFLICT", 
                      "K_CONSTRAINT", "K_CREATE", "K_CROSS", "K_CURRENT_DATE", 
                      "K_CURRENT_TIME", "K_CURRENT_TIMESTAMP", "K_DATABASE", 
                      "K_DEFAULT", "K_DEFERRABLE", "K_DEFERRED", "K_DELETE", 
                      "K_DESC", "K_DETACH", "K_DISTINCT", "K_DROP", "K_EACH", 
                      "K_ELSE", "K_END", "K_ESCAPE", "K_EXCEPT", "K_EXCLUSIVE", 
                      "K_EXISTS", "K_EXPLAIN", "K_FAIL", "K_FOR", "K_FOREIGN", 
                      "K_FROM", "K_FULL", "K_GLOB", "K_GROUP", "K_HAVING", 
                      "K_IF", "K_IGNORE", "K_IMMEDIATE", "K_IN", "K_INDEX", 
                      "K_INDEXED", "K_INITIALLY", "K_INNER", "K_INSERT", 
                      "K_INSTEAD", "K_INTERSECT", "K_INTO", "K_IS", "K_ISNULL", 
                      "K_JOIN", "K_KEY", "K_LEFT", "K_LIKE", "K_LIMIT", 
                      "K_MATCH", "K_NATURAL", "K_NO", "K_NOT", "K_NOTNULL", 
                      "K_NULL", "K_OF", "K_OFFSET", "K_ON", "K_OR", "K_ORDER", 
                      "K_OUTER", "K_PLAN", "K_PRAGMA", "K_PRIMARY", "K_QUERY", 
                      "K_RAISE", "K_RECURSIVE", "K_REFERENCES", "K_REGEXP", 
                      "K_REINDEX", "K_RELEASE", "K_RENAME", "K_REPLACE", 
                      "K_RESTRICT", "K_RIGHT", "K_ROLLBACK", "K_ROW", "K_SAVEPOINT", 
                      "K_SELECT", "K_SET", "K_TABLE", "K_TEMP", "K_TEMPORARY", 
                      "K_THEN", "K_TO", "K_TRANSACTION", "K_TRIGGER", "K_UNION", 
                      "K_UNIQUE", "K_UPDATE", "K_USING", "K_VACUUM", "K_VALUES", 
                      "K_VIEW", "K_VIRTUAL", "K_WHEN", "K_WHERE", "K_WITH", 
                      "K_WITHOUT", "IDENTIFIER", "NUMERIC_LITERAL", "BIND_PARAMETER", 
                      "STRING_LITERAL", "BLOB_LITERAL", "SINGLE_LINE_COMMENT", 
                      "MULTILINE_COMMENT", "SPACES", "UNEXPECTED_CHAR" ]

    RULE_select_stmt = 0
    RULE_select_core = 1
    RULE_from_clause = 2
    RULE_table_or_subquery = 3
    RULE_table_name = 4
    RULE_result_column = 5
    RULE_unary_expr = 6
    RULE_expr = 7
    RULE_signed_number = 8
    RULE_literal_value = 9

    ruleNames =  [ "select_stmt", "select_core", "from_clause", "table_or_subquery", 
                   "table_name", "result_column", "unary_expr", "expr", 
                   "signed_number", "literal_value" ]

    EOF = Token.EOF
    SCOL=1
    DOT=2
    OPEN_PAR=3
    CLOSE_PAR=4
    COMMA=5
    ASSIGN=6
    STAR=7
    PLUS=8
    MINUS=9
    TILDE=10
    PIPE2=11
    DIV=12
    MOD=13
    LT2=14
    GT2=15
    AMP=16
    PIPE=17
    LT=18
    LT_EQ=19
    GT=20
    GT_EQ=21
    EQ=22
    NOT_EQ1=23
    NOT_EQ2=24
    K_ABORT=25
    K_ACTION=26
    K_ADD=27
    K_AFTER=28
    K_ALL=29
    K_ALTER=30
    K_ANALYZE=31
    K_AND=32
    K_AS=33
    K_ASC=34
    K_ATTACH=35
    K_AUTOINCREMENT=36
    K_BEFORE=37
    K_BEGIN=38
    K_BETWEEN=39
    K_BY=40
    K_CASCADE=41
    K_CASE=42
    K_CAST=43
    K_CHECK=44
    K_COLLATE=45
    K_COLUMN=46
    K_COMMIT=47
    K_CONFLICT=48
    K_CONSTRAINT=49
    K_CREATE=50
    K_CROSS=51
    K_CURRENT_DATE=52
    K_CURRENT_TIME=53
    K_CURRENT_TIMESTAMP=54
    K_DATABASE=55
    K_DEFAULT=56
    K_DEFERRABLE=57
    K_DEFERRED=58
    K_DELETE=59
    K_DESC=60
    K_DETACH=61
    K_DISTINCT=62
    K_DROP=63
    K_EACH=64
    K_ELSE=65
    K_END=66
    K_ESCAPE=67
    K_EXCEPT=68
    K_EXCLUSIVE=69
    K_EXISTS=70
    K_EXPLAIN=71
    K_FAIL=72
    K_FOR=73
    K_FOREIGN=74
    K_FROM=75
    K_FULL=76
    K_GLOB=77
    K_GROUP=78
    K_HAVING=79
    K_IF=80
    K_IGNORE=81
    K_IMMEDIATE=82
    K_IN=83
    K_INDEX=84
    K_INDEXED=85
    K_INITIALLY=86
    K_INNER=87
    K_INSERT=88
    K_INSTEAD=89
    K_INTERSECT=90
    K_INTO=91
    K_IS=92
    K_ISNULL=93
    K_JOIN=94
    K_KEY=95
    K_LEFT=96
    K_LIKE=97
    K_LIMIT=98
    K_MATCH=99
    K_NATURAL=100
    K_NO=101
    K_NOT=102
    K_NOTNULL=103
    K_NULL=104
    K_OF=105
    K_OFFSET=106
    K_ON=107
    K_OR=108
    K_ORDER=109
    K_OUTER=110
    K_PLAN=111
    K_PRAGMA=112
    K_PRIMARY=113
    K_QUERY=114
    K_RAISE=115
    K_RECURSIVE=116
    K_REFERENCES=117
    K_REGEXP=118
    K_REINDEX=119
    K_RELEASE=120
    K_RENAME=121
    K_REPLACE=122
    K_RESTRICT=123
    K_RIGHT=124
    K_ROLLBACK=125
    K_ROW=126
    K_SAVEPOINT=127
    K_SELECT=128
    K_SET=129
    K_TABLE=130
    K_TEMP=131
    K_TEMPORARY=132
    K_THEN=133
    K_TO=134
    K_TRANSACTION=135
    K_TRIGGER=136
    K_UNION=137
    K_UNIQUE=138
    K_UPDATE=139
    K_USING=140
    K_VACUUM=141
    K_VALUES=142
    K_VIEW=143
    K_VIRTUAL=144
    K_WHEN=145
    K_WHERE=146
    K_WITH=147
    K_WITHOUT=148
    IDENTIFIER=149
    NUMERIC_LITERAL=150
    BIND_PARAMETER=151
    STRING_LITERAL=152
    BLOB_LITERAL=153
    SINGLE_LINE_COMMENT=154
    MULTILINE_COMMENT=155
    SPACES=156
    UNEXPECTED_CHAR=157

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Select_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select_core(self):
            return self.getTypedRuleContext(JsonSQLParser.Select_coreContext,0)


        def getRuleIndex(self):
            return JsonSQLParser.RULE_select_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_stmt" ):
                listener.enterSelect_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_stmt" ):
                listener.exitSelect_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect_stmt" ):
                return visitor.visitSelect_stmt(self)
            else:
                return visitor.visitChildren(self)




    def select_stmt(self):

        localctx = JsonSQLParser.Select_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_select_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.select_core()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Select_coreContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_SELECT(self):
            return self.getToken(JsonSQLParser.K_SELECT, 0)

        def result_column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JsonSQLParser.Result_columnContext)
            else:
                return self.getTypedRuleContext(JsonSQLParser.Result_columnContext,i)


        def from_clause(self):
            return self.getTypedRuleContext(JsonSQLParser.From_clauseContext,0)


        def getRuleIndex(self):
            return JsonSQLParser.RULE_select_core

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_core" ):
                listener.enterSelect_core(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_core" ):
                listener.exitSelect_core(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect_core" ):
                return visitor.visitSelect_core(self)
            else:
                return visitor.visitChildren(self)




    def select_core(self):

        localctx = JsonSQLParser.Select_coreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_select_core)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(JsonSQLParser.K_SELECT)
            self.state = 23
            self.result_column()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JsonSQLParser.COMMA:
                self.state = 24
                self.match(JsonSQLParser.COMMA)
                self.state = 25
                self.result_column()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            _la = self._input.LA(1)
            if _la==JsonSQLParser.K_FROM:
                self.state = 31
                self.from_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class From_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_FROM(self):
            return self.getToken(JsonSQLParser.K_FROM, 0)

        def table_or_subquery(self):
            return self.getTypedRuleContext(JsonSQLParser.Table_or_subqueryContext,0)


        def getRuleIndex(self):
            return JsonSQLParser.RULE_from_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrom_clause" ):
                listener.enterFrom_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrom_clause" ):
                listener.exitFrom_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFrom_clause" ):
                return visitor.visitFrom_clause(self)
            else:
                return visitor.visitChildren(self)




    def from_clause(self):

        localctx = JsonSQLParser.From_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_from_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(JsonSQLParser.K_FROM)
            self.state = 35
            self.table_or_subquery()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Table_or_subqueryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table_name(self):
            return self.getTypedRuleContext(JsonSQLParser.Table_nameContext,0)


        def getRuleIndex(self):
            return JsonSQLParser.RULE_table_or_subquery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_or_subquery" ):
                listener.enterTable_or_subquery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_or_subquery" ):
                listener.exitTable_or_subquery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_or_subquery" ):
                return visitor.visitTable_or_subquery(self)
            else:
                return visitor.visitChildren(self)




    def table_or_subquery(self):

        localctx = JsonSQLParser.Table_or_subqueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_table_or_subquery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.table_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Table_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(JsonSQLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return JsonSQLParser.RULE_table_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_name" ):
                listener.enterTable_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_name" ):
                listener.exitTable_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_name" ):
                return visitor.visitTable_name(self)
            else:
                return visitor.visitChildren(self)




    def table_name(self):

        localctx = JsonSQLParser.Table_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_table_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(JsonSQLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Result_columnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(JsonSQLParser.ExprContext,0)


        def getRuleIndex(self):
            return JsonSQLParser.RULE_result_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResult_column" ):
                listener.enterResult_column(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResult_column" ):
                listener.exitResult_column(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResult_column" ):
                return visitor.visitResult_column(self)
            else:
                return visitor.visitChildren(self)




    def result_column(self):

        localctx = JsonSQLParser.Result_columnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_result_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Unary_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr(self):
            return self.getTypedRuleContext(JsonSQLParser.ExprContext,0)


        def K_NOT(self):
            return self.getToken(JsonSQLParser.K_NOT, 0)

        def getRuleIndex(self):
            return JsonSQLParser.RULE_unary_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_expr" ):
                listener.enterUnary_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_expr" ):
                listener.exitUnary_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_expr" ):
                return visitor.visitUnary_expr(self)
            else:
                return visitor.visitChildren(self)




    def unary_expr(self):

        localctx = JsonSQLParser.Unary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_unary_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JsonSQLParser.PLUS) | (1 << JsonSQLParser.MINUS) | (1 << JsonSQLParser.TILDE))) != 0) or _la==JsonSQLParser.K_NOT):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 44
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def literal_value(self):
            return self.getTypedRuleContext(JsonSQLParser.Literal_valueContext,0)


        def unary_expr(self):
            return self.getTypedRuleContext(JsonSQLParser.Unary_exprContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JsonSQLParser.ExprContext)
            else:
                return self.getTypedRuleContext(JsonSQLParser.ExprContext,i)


        def getRuleIndex(self):
            return JsonSQLParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = JsonSQLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            token = self._input.LA(1)
            if token in [JsonSQLParser.K_CURRENT_DATE, JsonSQLParser.K_CURRENT_TIME, JsonSQLParser.K_CURRENT_TIMESTAMP, JsonSQLParser.K_NULL, JsonSQLParser.NUMERIC_LITERAL, JsonSQLParser.STRING_LITERAL, JsonSQLParser.BLOB_LITERAL]:
                self.state = 47
                self.literal_value()

            elif token in [JsonSQLParser.PLUS, JsonSQLParser.MINUS, JsonSQLParser.TILDE, JsonSQLParser.K_NOT]:
                self.state = 48
                self.unary_expr()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 60
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = JsonSQLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 52
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==JsonSQLParser.PLUS or _la==JsonSQLParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 53
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = JsonSQLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 55
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JsonSQLParser.LT2) | (1 << JsonSQLParser.GT2) | (1 << JsonSQLParser.AMP) | (1 << JsonSQLParser.PIPE))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 56
                        self.expr(3)
                        pass

                    elif la_ == 3:
                        localctx = JsonSQLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 57
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 58
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JsonSQLParser.LT) | (1 << JsonSQLParser.LT_EQ) | (1 << JsonSQLParser.GT) | (1 << JsonSQLParser.GT_EQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 59
                        self.expr(2)
                        pass

             
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Signed_numberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERIC_LITERAL(self):
            return self.getToken(JsonSQLParser.NUMERIC_LITERAL, 0)

        def getRuleIndex(self):
            return JsonSQLParser.RULE_signed_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSigned_number" ):
                listener.enterSigned_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSigned_number" ):
                listener.exitSigned_number(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSigned_number" ):
                return visitor.visitSigned_number(self)
            else:
                return visitor.visitChildren(self)




    def signed_number(self):

        localctx = JsonSQLParser.Signed_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_signed_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            _la = self._input.LA(1)
            if _la==JsonSQLParser.PLUS or _la==JsonSQLParser.MINUS:
                self.state = 65
                _la = self._input.LA(1)
                if not(_la==JsonSQLParser.PLUS or _la==JsonSQLParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()


            self.state = 68
            self.match(JsonSQLParser.NUMERIC_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERIC_LITERAL(self):
            return self.getToken(JsonSQLParser.NUMERIC_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(JsonSQLParser.STRING_LITERAL, 0)

        def BLOB_LITERAL(self):
            return self.getToken(JsonSQLParser.BLOB_LITERAL, 0)

        def K_NULL(self):
            return self.getToken(JsonSQLParser.K_NULL, 0)

        def K_CURRENT_TIME(self):
            return self.getToken(JsonSQLParser.K_CURRENT_TIME, 0)

        def K_CURRENT_DATE(self):
            return self.getToken(JsonSQLParser.K_CURRENT_DATE, 0)

        def K_CURRENT_TIMESTAMP(self):
            return self.getToken(JsonSQLParser.K_CURRENT_TIMESTAMP, 0)

        def getRuleIndex(self):
            return JsonSQLParser.RULE_literal_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_value" ):
                listener.enterLiteral_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_value" ):
                listener.exitLiteral_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_value" ):
                return visitor.visitLiteral_value(self)
            else:
                return visitor.visitChildren(self)




    def literal_value(self):

        localctx = JsonSQLParser.Literal_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_literal_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JsonSQLParser.K_CURRENT_DATE) | (1 << JsonSQLParser.K_CURRENT_TIME) | (1 << JsonSQLParser.K_CURRENT_TIMESTAMP))) != 0) or ((((_la - 104)) & ~0x3f) == 0 and ((1 << (_la - 104)) & ((1 << (JsonSQLParser.K_NULL - 104)) | (1 << (JsonSQLParser.NUMERIC_LITERAL - 104)) | (1 << (JsonSQLParser.STRING_LITERAL - 104)) | (1 << (JsonSQLParser.BLOB_LITERAL - 104)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




