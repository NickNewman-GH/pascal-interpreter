from .tokens import Token

class Node:

    def __str__(self):
        return f"{self.__class__.__name__}"

class Number(Node):

    def __init__(self, token: Token):
        self.token = token

    def __str__(self):
        return f"Number({self.token.value})"

class BinOp(Node):

    def __init__(self, left: Node, op: Token, right: Node):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f"BinOp<{self.op.value}>({self.left}, {self.right})"

class UnaryOp(Node):

    def __init__(self, op: Token, right: Node):
        self.op = op
        self.right = right

    def __str__(self):
        return f"UnaryOp<{self.op.value}>({self.right})"

class Empty(Node):
    ...

class Variable(Node):

    def __init__(self, variable: Token):
        self.name = variable.value

    def __str__(self):
        return f"Variable<{self.name}>"

class Assignment(Node):

    def __init__(self, variable: Node, op: Token, expr: Node):
        self.variable = variable
        self.op = op
        self.expr = expr

    def __str__(self):
        return f"Assignment<{self.variable}>{self.op}({self.expr})"

class StatementList(Node):

    def __init__(self):
        self.statements = []

    def __str__(self):
        return f"StatementList{[str(elem) for elem in self.statements]}"