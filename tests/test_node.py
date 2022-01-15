from interpreter import (Assignment, BinOp, Empty, Number, StatementList,
                         Token, TokenType, UnaryOp, Variable)


class TestNode:

    def test_empty(self):
        node = Empty()
        assert str(node) ==  'Empty'
    
    def test_number(self):
        node = Number(Token(TokenType.NUMBER, '356'))
        assert node.token.type_ == TokenType.NUMBER and node.token.value == '356'
        assert str(node) == 'Number(356)'

    def test_variable(self):
        node = Variable(Token(TokenType.VARIABLE, 'x'))
        assert node.token.type_ == TokenType.VARIABLE and node.token.value == 'x'
        assert str(node) == 'Variable(x)'
        
    def test_binop(self):
        node = BinOp(Number(Token(TokenType.NUMBER, '56')), Token(TokenType.PLUS, '+'), Variable(Token(TokenType.VARIABLE, 'b')))
        assert node.left.token.type_ == TokenType.NUMBER and node.left.token.value == '56'
        assert node.right.token.type_ == TokenType.VARIABLE and node.right.token.value == 'b'
        assert node.op.type_ == TokenType.PLUS and node.op.value == '+'
        assert str(node) == 'BinOp(Number(56), Token(TokenType.PLUS, +), Variable(b))'

    def test_unop(self):
        node = UnaryOp(Token(TokenType.MINUS, '-'), Variable(Token(TokenType.VARIABLE, 'c')))
        assert node.op.type_ == TokenType.MINUS and node.op.value == '-'
        assert node.right.token.type_ == TokenType.VARIABLE and node.right.token.value == 'c'
        assert str(node) == 'UnaryOp(Token(TokenType.MINUS, -), Variable(c))'
    
    def test_assignment(self):
        node = Assignment(Variable(Token(TokenType.VARIABLE, 'c')), Token(TokenType.ASSIGN, ':='), Number(Token(TokenType.NUMBER, '3')))
        assert node.left.token.type_ == TokenType.VARIABLE and node.left.token.value == 'c'
        assert node.right.token.type_ == TokenType.NUMBER and node.right.token.value == '3'
        assert node.op.type_ == TokenType.ASSIGN and node.op.value == ':='
        assert str(node) == 'Assignment(Variable(c), Token(TokenType.ASSIGN, :=), Number(3))'

    def test_statement_list(self):
        node = StatementList()
        assignment = Assignment(Variable(Token(TokenType.VARIABLE, 'c')), Token(TokenType.ASSIGN, ':='), Number(Token(TokenType.NUMBER, '3')))
        node.statements.append(assignment)
        assert node.statements[0].left.token.type_ == TokenType.VARIABLE and node.statements[0].left.token.value == 'c'
        assert node.statements[0].right.token.type_ == TokenType.NUMBER and node.statements[0].right.token.value == '3'
        assert node.statements[0].op.type_ == TokenType.ASSIGN and node.statements[0].op.value == ':='
        assert str(node) == "StatementList['Assignment(Variable(c), Token(TokenType.ASSIGN, :=), Number(3))']"
    