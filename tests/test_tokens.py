import pytest
from interpreter import Token, TokenType


class TestToken:
    
    def test_creation(self):
        token = Token(TokenType.NUMBER, '-5.2')
        assert token.type_ == TokenType.NUMBER and token.value == '-5.2'

        token = Token(TokenType.BEGIN, 'BEGIN')
        assert token.type_ == TokenType.BEGIN and token.value == 'BEGIN'

        with pytest.raises(AttributeError):
            token = Token(TokenType.QUIT, 'ESC')
    
    def test_str(self):
        token = Token(TokenType.NUMBER, 'sometext')
        assert str(token) == 'Token(TokenType.NUMBER, sometext)'
    
    def test_repr(self):
        token = Token(TokenType.VARIABLE, 'anothertext')
        assert repr(token) == 'Token(TokenType.VARIABLE, anothertext)'
