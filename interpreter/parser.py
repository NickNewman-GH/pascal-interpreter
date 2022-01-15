from .tokens import TokenType, Token
from .lexer import Lexer
from .node import Empty, Node, Number, BinOp, UnaryOp, Assignment, Variable, StatementList

class ParserException(Exception):
    pass

class Parser():
    
    def __init__(self):
        self._current_token: Token = None
        self._lexer = Lexer()

    def _check_token_type(self, type_: TokenType):
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            raise ParserException("Invalid token order")

    def _factor(self) -> Node:
        token = self._current_token
        if token.type_ == TokenType.MINUS:
            self._check_token_type(TokenType.MINUS)
            return UnaryOp(token, self._factor())
        if token.type_ == TokenType.PLUS:
            self._check_token_type(TokenType.PLUS)
            return UnaryOp(token, self._factor())
        if token.type_ == TokenType.NUMBER:
            self._check_token_type(TokenType.NUMBER)
            return Number(token)
        if token.type_ == TokenType.LPAREN:
            self._check_token_type(TokenType.LPAREN)
            result = self._expr()
            self._check_token_type(TokenType.RPAREN)
            return result
        if token.type_ == TokenType.VARIABLE:
            return self._variable()
        raise ParserException("Invalid factor")

    def _pow(self) -> Node:
        result = self._factor()
        op = TokenType.POW
        while self._current_token.type_ == op:
            token = self._current_token
            if token.type_ == TokenType.POW:
                self._check_token_type(TokenType.POW)
            result = BinOp(result, token, self._factor())
        return result

    def _term(self) -> Node:
        result = self._pow()
        ops = [TokenType.MUL, TokenType.DIV]
        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.MUL:
                self._check_token_type(TokenType.MUL)
            else:
                self._check_token_type(TokenType.DIV)
            result = BinOp(result, token, self._pow())
        return result
        
    def _expr(self) -> Node:
        result = self._term()
        ops = [TokenType.PLUS, TokenType.MINUS]
        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.PLUS:
                self._check_token_type(TokenType.PLUS)
            else:
                self._check_token_type(TokenType.MINUS)
            result = BinOp(result, token, self._term())
        return result
    
    def _variable(self) -> Node:
        token = self._current_token
        self._check_token_type(TokenType.VARIABLE)
        variable = Variable(token)
        return variable

    def _assignment(self) -> Node:
        variable = self._variable()
        self._check_token_type(TokenType.ASSIGN)
        expr = self._expr()
        return Assignment(variable, expr)

    def _statement(self) -> Node:
        if self._current_token.type_ == TokenType.BEGIN:
            return self._complex_statement()
        elif self._current_token.type_ == TokenType.VARIABLE:
            return self._assignment()
        else:
            return Empty()

    def _statement_list(self) -> Node:
        statement_list = StatementList()
        statement_list.statements.append(self._statement())
        while self._current_token.type_ == TokenType.SEMICOLON:
            self._check_token_type(TokenType.SEMICOLON)
            if self._current_token.type_ != TokenType.END:
                statement_list.statements.append(self._statement())
            else:
                self._check_token_type(TokenType.END)
                return statement_list
        self._check_token_type(TokenType.END)
        return statement_list

    def _complex_statement(self) -> Node:
        self._check_token_type(TokenType.BEGIN)
        statement_list = self._statement_list()
        self._check_token_type(TokenType.END)
        return statement_list

    def _program(self) -> Node:
        complex_statement = self._complex_statement()
        self._check_token_type(TokenType.DOT)
        return complex_statement

    def __call__(self, text : str) -> Node:
        return self.parse(text)

    def parse(self, text : str) -> Node:
        self._lexer.init(text)
        self._current_token = self._lexer.next()
        return self._program()