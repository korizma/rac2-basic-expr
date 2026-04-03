from antlr4 import *
from generated.ExprLexer import ExprLexer
from generated.ExprParser import ExprParser 

from .Visitor import Visitor

def main():
    example_file = "examples/example.izraz"

    query = InputStream(open(example_file).read())
    lexer = ExprLexer(query)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"Found {parser.getNumberOfSyntaxErrors()} syntax errors. Exiting.")
        return

    print("Parse tree:")
    print(tree.toStringTree(recog=parser))

    visitor = Visitor()

    res = tree.accept(visitor)
    print(res)

main()