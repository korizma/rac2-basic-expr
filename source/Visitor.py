from generated.ExprVisitor import ExprVisitor
from generated.ExprParser import ExprParser

class Visitor(ExprVisitor):
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        print("Visited Program")
        ctx.expr().accept(self)

    def visitExpr(self, ctx:ExprParser.ExprContext):
        print("Visited Expression")
        for term in ctx.term():
            term.accept(self)

    def visitTerm(self, ctx:ExprParser.TermContext):
        print("Visited Term")