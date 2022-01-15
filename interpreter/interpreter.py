from os import PathLike
from types import resolve_bases
from .tokens import TokenType, Token
from .lexer import Lexer
from typing import Union
from .node import Empty, Node, Number, BinOp, UnaryOp, Assignment, Variable, StatementList
import operator


class InterpreterException(Exception):
    pass

class Interpreter():

    def __init__(self) -> None:
        self._variables = {}

    def __call__(self, tree: Node) -> dict:
        return self.interpret(tree)
    
    def interpret(self, tree: Node) -> dict:
        self._visit(tree)
        return self._variables

    def _visit(self, node: Node):
        if isinstance(node, Number):
            return self._visit_number(node)
        elif isinstance(node, BinOp):
            return self._visit_binop(node)
        elif isinstance(node, UnaryOp):
            return self._visit_unop(node)
        elif isinstance(node, Empty):
            return self._visit_empty(node)
        elif isinstance(node, Assignment):
            return self._visit_assignment(node)
        elif isinstance(node, Variable):
            return self._visit_variable(node)
        elif isinstance(node, StatementList):
            return self._visit_statement_list(node)
        raise InterpreterException("invalid node")

    def _visit_number(self, node: Number) -> Union[int, float]:
        try:
            return int(node.token.value)
        except ValueError:
            return float(node.token.value)

    def _visit_unop(self, node: UnaryOp) -> float:
        op = node.op
        if op.type_ == TokenType.MINUS:
            return -self._visit(node.right)
        elif op.type_ == TokenType.PLUS:
            return self._visit(node.right)
        raise InterpreterException("invalid unary operator")

    def _visit_binop(self, node: BinOp) -> float:
        op = node.op
        binop = {TokenType.PLUS: operator.add,
                 TokenType.MINUS: operator.sub,
                 TokenType.DIV: operator.truediv,
                 TokenType.MUL: operator.mul,
                 TokenType.POW: operator.pow}.get(op.type_)
        if binop:
            return binop(self._visit(node.left), self._visit(node.right))
        raise InterpreterException("invalid operator")
    
    def _visit_empty(self, node: Empty) -> None:
        ...

    def _visit_assignment(self, node: Assignment) -> None:
        self._variables[node.left.token.value] = self._visit(node.right)

    def _visit_variable(self, node: Variable) -> float:
        if node.token.value not in self._variables:
            raise InterpreterException(f"Name {node.token.value} is not defined")
        return self._variables[node.token.value]

    def _visit_statement_list(self, node: StatementList) -> None:
        for statement in node.statements:
            self._visit(statement)