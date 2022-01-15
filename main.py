from interpreter import Interpreter
from interpreter import Parser
from interpreter import Lexer
from interpreter import TokenType
import interpreter

if __name__ == "__main__":
    lexer = Lexer()
    parser = Parser()

    interpreter = Interpreter()

    result = interpreter(parser(
    """
    BEGIN
        x := 25;
        BEGIN
            f := 34;
            f := f - 30
        END;
        y:= x + 3 ^ f;
    END.
    """))

print(result)