grammar Expr;

program
    :  (expr SEMI)+ EOF
    ;

expr: addExpr;

addExpr: mulExpr (ADDOP mulExpr)*;

mulExpr: parExpr (MULOP parExpr)*;

parExpr: '(' expr ')' | term;

term: INT;

SEMI: ';';

ADDOP: '+' | '-';

MULOP: '*' | '/';

INT
    : [0-9]+
    ;

WS
    : [ \t\r\n]+ -> skip
    ;