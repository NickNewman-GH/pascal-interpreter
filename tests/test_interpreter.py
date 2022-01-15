import pytest
from interpreter import Interpreter, InterpreterException, Parser, TokenType


@pytest.fixture
def text():
    return """
    BEGIN
        y := +2.0;
        begin
        end;
        a := -3;
        a := a ^ 2;
        b := (a + 10);
        begin
        s := 5
        end;
        b := b * y;
        y := y / 4;
        y := y - 2;
    END.
    """

@pytest.fixture
def result():
    return {'y': -1.5, 'a': 9, 'b': 38, 's': 5}

class TestInterpreter:

    def test_creation(self):
        interpreter = Interpreter()
        assert interpreter._variables == {}

    def test_interpret(self, text, result):
        parser = Parser()
        tree = parser(text)
        interpreter = Interpreter()
        assert interpreter.interpret(tree) == result

    def test_call(self, text, result):
        parser = Parser()
        tree = parser(text)
        interpreter = Interpreter()
        assert interpreter(tree) == result
    
    def test_errors(self):
        parser = Parser()
        interpreter = Interpreter()
        with pytest.raises(InterpreterException):
            interpreter('text')

        tree = parser('BEGIN a := b END.')
        with pytest.raises(InterpreterException):
            interpreter(tree)

    def test_forced_errors(self):
        parser = Parser()
        interpreter = Interpreter()

        tree = parser('BEGIN a := -2 END.')
        tree.statements[0].right.op.type_ = TokenType.MUL
        with pytest.raises(InterpreterException):
            interpreter(tree)
        
        tree = parser('BEGIN a := 2 + 3 END.')
        tree.statements[0].right.op.type_ = TokenType.LPAREN
        with pytest.raises(InterpreterException):
            interpreter(tree)
