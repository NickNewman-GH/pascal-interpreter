import pytest
from interpreter import Parser, ParserException


@pytest.fixture
def text():
    return """
    BEGIN
        y := +2; begin end; a := -3;
        a := a ^ 2; b := (a + 10);
        begin s := 5 end;
        b := b * y; y := y / 4; y := y - 2;
    END.
    """

@pytest.fixture
def output_strings():
    return ['Assignment(Variable(y), Token(TokenType.ASSIGN, :=), UnaryOp(Token(TokenType.PLUS, +), Number(2)))',
    "StatementList['Empty']",
    'Assignment(Variable(a), Token(TokenType.ASSIGN, :=), UnaryOp(Token(TokenType.MINUS, -), Number(3)))',
    'Assignment(Variable(a), Token(TokenType.ASSIGN, :=), BinOp(Variable(a), Token(TokenType.POW, ^), Number(2)))',
    'Assignment(Variable(b), Token(TokenType.ASSIGN, :=), BinOp(Variable(a), Token(TokenType.PLUS, +), Number(10)))',
    "StatementList['Assignment(Variable(s), Token(TokenType.ASSIGN, :=), Number(5))']",
    'Assignment(Variable(b), Token(TokenType.ASSIGN, :=), BinOp(Variable(b), Token(TokenType.MUL, *), Variable(y)))',
    'Assignment(Variable(y), Token(TokenType.ASSIGN, :=), BinOp(Variable(y), Token(TokenType.DIV, /), Number(4)))',
    'Assignment(Variable(y), Token(TokenType.ASSIGN, :=), BinOp(Variable(y), Token(TokenType.MINUS, -), Number(2)))']

class TestParser:
    
    def test_creation(self):
        parser = Parser()
        assert parser._current_token == None
        
    def test_parse(self, text, output_strings):
        parser = Parser()
        
        result = parser.parse(text)

        for index, assignment in enumerate(result.statements):
            assert str(assignment) == output_strings[index]

    def test_factor_error(self):
        parser = Parser()
        with pytest.raises(ParserException):
            parser.parse("""BEGIN y := END; END.""")

    def test_check_token_type(self):
        parser = Parser()
        with pytest.raises(ParserException):
            parser.parse("""BEGIN y 2; END.""")
    
    def test_call(self):
        parser = Parser()
        result = parser("""BEGIN y := 2; END.""")
        assert str(result.statements[0]) == 'Assignment(Variable(y), Token(TokenType.ASSIGN, :=), Number(2))'
