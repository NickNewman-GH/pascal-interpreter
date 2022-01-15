from interpreter import Interpreter
from interpreter import Parser
from interpreter import Lexer
from interpreter import TokenType
import interpreter

if __name__ == "__main__":
    parser = Parser()
    interpreter = Interpreter()

    print(interpreter(parser(
    """
    BEGIN
        y := 2;
        BEGIN
        END;
        x := 11;
    END.
    """)))

#     lexer = Lexer()
#     lexer.init(
#     """
# BEGIN
#     y := 2;
#     BEGIN
#         a := 3;
#         a := a;
#         b := 10 + a + 10 * y / 4;
#         c := a - b
#     END;
#     x := 11;
# END.
#     """)
#     token = lexer.next()
#     while token.type_ != TokenType.EOS:
#         print(token)
#         token = lexer.next()
    # parcer = Parser()
    # interpreter = Interpreter()
    # tree = parcer.parse("--2 * (2 + 3)")
    # print(interpreter.interpret(tree))
    # tree = parcer.parse("+2 * 3 ^ -3")
    # print(interpreter.interpret(tree))
    # tree = parcer.parse("5-( 2 * 3)")
    # print(interpreter.interpret(tree))