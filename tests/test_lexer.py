import pytest
from interpreter import Lexer, LexerException, Token, TokenType


@pytest.fixture
def textsAndTokens():
    return {
        '     ':Token(TokenType.EOS, None), 
        ' 56.26':Token(TokenType.NUMBER, '56.26'), 
        ' + ':Token(TokenType.PLUS, '+'), 
        '- ':Token(TokenType.MINUS, '-'), 
        '*':Token(TokenType.MUL, '*'), 
        '/':Token(TokenType.DIV, '/'), 
        '^':Token(TokenType.POW, '^'), 
        '(':Token(TokenType.LPAREN, '('), 
        ') (':Token(TokenType.RPAREN, ')'), 
        '.':Token(TokenType.DOT, '.'), 
        ';':Token(TokenType.SEMICOLON, ';'), 
        ':=':Token(TokenType.ASSIGN, ':='), 
        ' BegIn\n':Token(TokenType.BEGIN, 'BegIn'), 
        'END':Token(TokenType.END, 'END'), 
        '\tx1':Token(TokenType.VARIABLE, 'x1')}

@pytest.fixture
def wrongNumbers():
    return ('2.', '9.9.26', '1..2')

class TestLexer:

    def test_creation(self):
        lexer = Lexer()
        assert (lexer._pos == -1 and 
        lexer._current_char == None and 
        lexer._text == '')

    def test_init(self):
        lexer = Lexer()
        lexer.init('sometext')
        assert (lexer._pos == 0 and 
        lexer._current_char == 's' and 
        lexer._text == 'sometext')

    def test_number(self, wrongNumbers):
        lexer = Lexer()
        for wrongNum in wrongNumbers:
            lexer.init(wrongNum)
            with pytest.raises(LexerException):
                lexer.next()

        lexer.init('2.6')
        token = lexer.next()
        assert token.type_ == TokenType.NUMBER and token.value == '2.6'

    def test_keywordOrVar(self):
        lexer = Lexer()
        lexer.init('x54ee')
        text = lexer._keywordOrVar()
        assert text == 'x54ee'
        
        lexer.init("x54eegjgyjyjvyjgyjgvjvgyjgyvjygvjgvyjgvyjyvgjgvyjygjtrgerq2423rwrtst")
        with pytest.raises(LexerException):
            lexer.next()
            
    def test_next(self, textsAndTokens):
        lexer = Lexer()
        for text in textsAndTokens:
            lexer.init(text)
            token = lexer.next()
            assert token.type_ == textsAndTokens[text].type_ and token.value == textsAndTokens[text].value

        lexer.init(' #')
        with pytest.raises(LexerException):
            lexer.next()

        lexer.init(' :23')
        with pytest.raises(LexerException):
            lexer.next()
