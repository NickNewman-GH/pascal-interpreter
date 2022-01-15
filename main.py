from interpreter import Interpreter
from interpreter import Parser
import interpreter

if __name__ == "__main__":

    texts = [
    '''
    BEGIN 
    END.
    '''
    ,
    '''
    BEGIN
        x:= 2 + 3 * (2 + 3);
        y:= 2 / 2 - 2 + 3 * ((1 + 1) + (1 + 1));
    END.
    '''
    ,
    '''
    BEGIN
        y := 2;
        BEGIN
            a := 3;
            a := a;
            b := 10 + a + 10 * y / 4;
            c := a - b
        END;
        x := 11;
    END.
    ''']

    parser = Parser()
    interpreter = Interpreter()

    for text in texts:
        result = interpreter(parser(text))
        print(result)