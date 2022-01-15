from enum import Enum, auto


class TokenType(Enum):

    # Expression
    NUMBER = auto()  # <integer or float>
    PLUS = auto()    # '+'
    MINUS = auto()   # '-'
    LPAREN = auto()  # '('
    RPAREN = auto()  # ')'
    MUL = auto()     # '*'
    DIV = auto()     # '/'
    POW = auto()     # '^'

    # Pascal stuff
    BEGIN = auto()      # 'BEGIN'
    END = auto()        # 'END'
    DOT = auto()        # '.'
    SEMICOLON = auto()  # ';'
    ASSIGN = auto()     # ':='
    VARIABLE = auto()   # <variable name>

    # Other
    EOS = auto()  # <end of string>

class Token():
    def __init__(self, type_: TokenType, value: str):
        self.type_ = type_
        self.value = value

    def __str__(self):
        return f"Token({self.type_}, {self.value})"

    def __repr__(self):
        return str(self)
