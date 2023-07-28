from enum import Enum


class fields(Enum):
    ID: str = "id"
    EMAIL: str = "email"
    PASS: str = "password"


class signs(Enum):
    EQ: str = "=="
    PLUS: str = "+"
    MINUS: str = "-"
    GT: str = ">"
    LT: str = "<"
    GE: str = ">="
    LE: str = "<="
