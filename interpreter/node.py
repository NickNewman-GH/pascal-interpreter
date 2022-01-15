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
        return f"BinOp({self.left}, {self.op}, {self.right})"

class UnaryOp(Node):

    def __init__(self, op: Token, right: Node):
        self.op = op
        self.right = right

    def __str__(self):
        return f"UnaryOp({self.op}, {self.right})"

class Empty(Node):
    ...

class Variable(Node):

    def __init__(self, variable: Token):
        self.token = variable

    def __str__(self):
        return f"Variable({self.token.value})"

class Assignment(Node):

    def __init__(self, left: Node, op: Token, right: Node):
        self.left = left  # <variable>
        self.op = op  # <operator>
        self.right = right  # <expr>

    def __str__(self):
        return f"Assignment({self.left}, {self.op}, {self.right})"

class StatementList(Node):

    def __init__(self):
        self.statements = []

    def __str__(self):
        return f"StatementList{[str(elem) for elem in self.statements]}"