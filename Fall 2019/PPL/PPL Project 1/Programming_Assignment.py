from enum import Enum
from tree import Tree
import sys

# ========================================================================================================
# Authors: Joshue Hoshiko & Gerom Pagaduan
# Class: CS 3210 - Section 1
# Programming Assignment 1
# September 28, 2019
#
# This program contains a Lexical Analyzer, a Syntax Analyzer, and crates a bottom-up Parse Tree.
# We also received help and also helped Dan Reuter.
# ========================================================================================================

#========================================================================================================
#========================LEXICAL ANALYZER=================================================================
#========================================================================================================
# all char classes
class CharClass(Enum):
    EOF        = 1
    LETTER     = 2
    DIGIT      = 3
    OPERATOR   = 4
    PUNCTUATOR = 5
    QUOTE      = 6
    BLANK      = 7
    OTHER      = 8

# reads the next char from input and returns its class
def getChar(input):
    if len(input) == 0:
        return (None, CharClass.EOF)
    c = input[0].lower()
    if c.isalpha():
        return (c, CharClass.LETTER)
    if c.isdigit():
        return (c, CharClass.DIGIT)
    if c in ['+', '-', '*', '/', '>', '=', '<']:
        return (c, CharClass.OPERATOR)
    if c in ['.', ':', ',', ';', '(', ')', '{', '}']:
        return (c, CharClass.PUNCTUATOR)
    if c in [' ', '\n', '\t']:
        return (c, CharClass.BLANK)
    return (c, CharClass.OTHER)

# calls getChar and getChar until it returns a non-blank
def getNonBlank(input):
    ignore = ""
    while True:
        c, charClass = getChar(input)
        if charClass == CharClass.BLANK:
            input, ignore = addChar(input, ignore)
        else:
            return input

# adds the next char from input to lexeme, advancing the input by one char
def addChar(input, lexeme):
    if len(input) > 0:
        lexeme += input[0]
        input = input[1:]
    return (input, lexeme)

# all tokens
class Token(Enum):
    ADDITION     = 1
    ASSIGNMENT     = 2
    BEGIN     = 3
    BOOLEAN_TYPE     = 4
    COLON = 5
    DO    = 6
    ELSE   = 7
    END  = 8
    EQUAL  = 9
    FALSE = 10
    GREATER = 11
    GREATER_EQUAL = 12
    IDENTIFIER = 13
    IF = 14
    INTEGER_LITERAL = 15
    INTEGER_TYPE = 16
    LESS = 17
    LESS_EQUAL = 18
    MULTIPLICATION = 19
    PERIOD = 20
    PROGRAM = 21
    READ = 22
    SEMICOLON = 23
    SUBTRACTION = 24
    THEN = 25
    TRUE = 26
    VAR = 27
    WHILE = 28
    WRITE = 29

# lexeme to token conversion
lookup = {
    "+"      : Token.ADDITION,
    ":="      : Token.ASSIGNMENT,
    "begin"      : Token.BEGIN,
    "boolean"      : Token.BOOLEAN_TYPE,
    "Boolean"      : Token.BOOLEAN_TYPE,
    ":"      : Token.COLON,
    "do"      : Token.DO,
    "else"      : Token.ELSE,
    "end"      : Token.END,
    "false" : Token.FALSE,
    ">"      : Token.GREATER,
    ">="      : Token.GREATER_EQUAL,
    "if"      : Token.IF,
    "integer"      : Token.INTEGER_TYPE,
    "Integer"      : Token.INTEGER_TYPE,
    "<"      : Token.LESS,
    "<="      : Token.LESS_EQUAL,
    "*"      : Token.MULTIPLICATION,
    "."      : Token.PERIOD,
    "program"      : Token.PROGRAM,
    "read"      : Token.READ,
    ";"      : Token.SEMICOLON,
    "-"      : Token.SUBTRACTION,
    "then"      : Token.THEN,
    "true"      : Token.TRUE,
    "var" : Token.VAR,
    "while" : Token.WHILE,
    "write" : Token.WRITE
}

# returns the next (lexeme, token) pair or None if EOF is reached
def lex(input):
    input = getNonBlank(input)

    c, charClass = getChar(input)
    lexeme = ""

    # check EOF first
    if charClass == CharClass.EOF:
        return (input, None, None)

    if charClass == CharClass.LETTER:
        while True:
            input, lexeme = addChar(input, lexeme)
            c, charClass = getChar(input)
            if charClass != CharClass.LETTER:
                if charClass != CharClass.DIGIT:
                    break
        if lexeme in lookup:
            return (input, lexeme, lookup[lexeme]) #if it's a keyword
        else:
            return (input, lexeme, Token.IDENTIFIER) #if it's not in the lookup, return identifier

    if charClass == CharClass.DIGIT:
        while True:
            input, lexeme = addChar(input, lexeme)
            c, charClass = getChar(input)
            if charClass != CharClass.DIGIT:
                break
        return (input, lexeme, Token.INTEGER_LITERAL)

    if charClass == CharClass.OPERATOR:
        while True:
            input, lexeme = addChar(input, lexeme)
            c, charClass = getChar(input)
            if charClass != CharClass.OPERATOR:
                break
        if lexeme in lookup:
            return (input, lexeme, lookup[lexeme])

    if charClass == CharClass.PUNCTUATOR:
        while True:
            input, lexeme = addChar(input, lexeme)
            c, charClass = getChar(input)
            if charClass != CharClass.OPERATOR:
                break
        if lexeme in lookup:
            return (input, lexeme, lookup[lexeme])

    raise Exception("Lexical Analyzer Error: unrecognized symbol was found!")

#========================================================================================================
#========================SYNTAX ANALYZER=================================================================
#========================================================================================================

def errorMessage(code):
    msg = "Error " + str(code).zfill(2) + ": "
    if code == 1:
        return msg + "Source file missing"
    if code == 2:
        return msg + "Couldn't open source file"
    if code == 3:
        return msg + "Lexical error"
    if code == 4:
        return msg + "Couldn't open grammar file"
    if code == 5:
        return msg + "Couldn't open SLR table file"
    if code == 6:
        return msg + "EOF expected"
    if code == 7:
        return msg + "Identifier expected"
    if code == 8:
        return msg + "Special word missing"
    if code == 9:
        return msg + "Symbol missing"
    if code == 10:
        return msg + "Data type expected"
    if code == 11:
        return msg + "Identifier or literal value expected"
    return msg + "Syntax error"

def loadGrammar(input):
   grammar = []
   for line in input:
       grammar.append(line.strip())
   return grammar

# returns the LHS (left hand side) of a given production
def getLHS(production):
   return production.split("->")[0].strip()

# returns the RHS (right hand side) of a given production
def getRHS(production):
   return production.split("->")[1].strip().split(" ")

# prints the productions of a given grammar, one per line
def printGrammar(grammar):
   for production in grammar:
       print(getLHS(production), end = " -> ")
       print(getRHS(production))

# reads the given input containing an SLR parsing table and returns the "actions" and "gotos" as dictionaries
def loadTable(input):

    actions = {}
    gotos = {}
    header = input.readline().strip().split(",")
    end = header.index("$")
    tokens = []
    for field in header[1:end + 1]:

        tokens.append(field)
        # tokens.append(int(field))
        variables = header[end + 1:]
    for line in input:
        row = line.strip().split(",")
        state = int(row[0])

        for i in range(len(tokens)):

            token = tokens[i]
            key = (state, token)
            value = row[i + 1]
            if len(value) == 0:
               value = None
            actions[key] = value
        for i in range(len(variables)):
            variable = variables[i]
            key = (state, variable)
            value = row[i + len(tokens) + 1]

            if len(value) == 0:
                value = None
            gotos[key] = value
    return (actions, gotos)

# prints the given actions, one per line
def printActions(actions):
    for key in actions:
        print(key, end = " -> ")
        print(actions[key])

# prints the given gotos, one per line
def printGotos(gotos):
    for key in gotos:
        print(key, end = " -> ")
        print(gotos[key])

def parse(input, grammar, actions, gotos):

   trees = []

   stack = []
   stack.append(0)
   while True:
       print("stack: ", end = "")
       print(stack, end = " ")
       print("\n")
       print("input: ", end = "")
       print("\n")

       print("stack: ", end = "")
       print(stack, end = " ")
       print("\n")
       print("input: ", end = "")
       print(input, end = " ")
       print("\n")
       state = stack[-1]
       token = input[0]
       action = actions[(state, token)]
       print("action: ", end = "")
       print(action)



       if action is None:
           if state == 1 and input[0] != "program":
               print(errorMessage(7))
           if state == 2 and input[0] != "var":
               print(errorMessage(8))
           if state == 24 and input[0] != ":=":
               print(errorMessage(9))
           if state == 30 and input[0] != ("boolean" or "integer"):
               print(errorMessage(10))
           if state == 44 and input[0] != ("+" or "-"):
                print(errorMessage(9))
           if state == 34 and input[0] != ("identifier" or "integer_literal" or "true" or "false"):
                print(errorMessage(11))
           if state == 8 and input[0] != "$":
               print(errorMessage(11))

           return None  # tree building update



       # shift operation
       if action[0] == 's':
           input.pop(0)
           stack.append(token)
           if len(action) == 3:
               state = int(action[1] + action[2])
           else:
               state = int(action[1])
           stack.append(state)

           tree = Tree()
           tree.data = token
           trees.append(tree)



       # reduce operation
       elif action[0] == 'r':
           if len(action) == 3:
               production = grammar[int(action[1] + action[2])]
           else:
               production = grammar[int(action[1])]
           lhs = getLHS(production)
           rhs = getRHS(production)
           for i in range(len(rhs) * 2):
               stack.pop()
           state = stack[-1]
           stack.append(lhs)
           stack.append(int(gotos[(state, lhs)]))

           newTree = Tree()
           newTree.data = lhs

           for tree in trees[-len(rhs):]:
               newTree.add(tree)

           trees = trees[:-len(rhs)]

           trees.append(newTree)



       # not a shift or reduce operation, must be an "accept" operation
       else:
           production = grammar[0]
           lhs = getLHS(production)
           rhs = getRHS(production)

           root = Tree()
           root.data = lhs
           for tree in trees:
               root.add(tree)

           return root

# main
if __name__ == "__main__":

    lexList = []
    # checks if source file was passed and if it exists
    if len(sys.argv) != 2:
        raise ValueError(errorMessage(1))
    source = open(sys.argv[1], "rt")
    if not source:
        raise IOError(errorMessage(2))
    input = source.read()
    output = []

    # main loop
    while True:
        input, lexeme, token = lex(input)
        if lexeme == None:
            break
        output.append((lexeme, token))

    # prints the output
    for (lexeme, token) in output:
        print(lexeme, token)
        if token == Token.IDENTIFIER:
            if lexeme in lookup:
                lexList.append(lexeme)
            else:
                lexList.append("identifier")
        elif token == Token.INTEGER_LITERAL:
            lexList.append("integer_literal")
        else:
            lexList.append(lexeme)
    lexList.append('$')

    input = open("ourGrammar.txt", "rt")
    grammar = loadGrammar(input)
    printGrammar(grammar)
    input.close()

    input = open("ourGrammarTable.csv", "rt")
    actions, gotos = loadTable(input)
    #printActions(actions)
    #printGotos(gotos)
    input.close()

    input = lexList

    # tree building update
    tree = parse(input, grammar, actions, gotos)
    if tree:
        print("Input is syntactically correct!")
        print("Parse Tree:")
        tree.print()
    else:
        print(errorMessage(99))
    source.close()