from dataclasses import dataclass


@dataclass
class fields:
    ID: str = "id"
    EMAIL: str = "email"
    PASS: str = "password"


class signs:
    EQ: str = "=="
    PLUS: str = "+"
    MINUS: str = "-"
    GT: str = ">"
    LT: str = "<"
    GE: str = ">="
    LE: str = "<="
