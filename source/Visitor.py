from generated.ExprVisitor import ExprVisitor
from generated.ExprParser import ExprParser

class Visitor(ExprVisitor):
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        print("Visited Program")
        res = []
        for expr in ctx.expr():
            res.append(expr.accept(self))

        return res

    def visitExpr(self, ctx:ExprParser.ExprContext):
        print("Visited Expression")
        if ctx.term() is not None:
            return ctx.term().accept(self)
        else:
            expr1_val = ctx.expr(0).accept(self)
            expr2_val = ctx.expr(1).accept(self)
            return expr1_val + expr2_val


    def visitTerm(self, ctx:ExprParser.TermContext):
        print("Visited Term")
        return int(ctx.INT().getText())