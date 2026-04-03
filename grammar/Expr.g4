grammar Expr;

program
    :  expr EOF
    ;

expr
    :  term OP term SEMI
    ;

term: INT;

SEMI: ';';

OP: '+';

INT
    : [0-9]+
    ;

WS
    : [ \t\r\n]+ -> skip
    ;