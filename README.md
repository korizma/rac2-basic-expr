# Expr Workshop

Small ANTLR + Python example project for parsing a simple expression grammar.

## Prerequisites

- Python 3
- Java
- ANTLR 4 command-line tools available as `antlr4` and `grun`

First follow the instructions for the `ANTLR4` Java tool at
[antlr4 repo instructions](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md)
You can find the installation instructions under the part `Installation`.

## Create and activate the virtual environment

Create the venv in `env/`:

```bash
python3 -m venv env
```

Activate it:

```bash
source env/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Generate the Python parser and visitor

The Python code imports generated files from the `generated/` directory, so regenerate ANTLR output there when the grammar changes:

```bash
cd grammar
antlr4 Expr.g4 -Dlanguage=Python3 -visitor -o ../generated 
```

This generates files such as:

- `generated/ExprLexer.py`
- `generated/ExprParser.py`
- `generated/ExprVisitor.py`

## Run the Python program

Run the project as a module from the repository root:

```bash
python -m source.main
```

This reads `examples/example.izraz`, builds the parse tree, prints it, and then visits the tree with `source/Visitor.py`.

## Run the ANTLR GUI parse tree viewer with `grun`

The GUI flow below matches what is in `guiView/run_gui.txt`.

Create new folder `guiView` and cd into it:

```bash
mkdir guiView && cd guiView
```

Copy the grammar into `guiView`:

```bash
cp ../grammar/Expr.g4 ./
```

Generate the Java ANTLR files:

```bash
antlr4 Expr.g4
```

Compile them:

```bash
javac *.java
```

Open the GUI parse tree viewer:

```bash
grun Expr program -gui < ../examples/example.izraz
```

## Notes

- `generated/` is gitignored, so regenerate it locally when needed.
- If you change the grammar, regenerate both the Python files in `generated/` and the Java files in `guiView/` before rerunning.
