from enum import Enum
from typing import List

from regast.core.expressions.expression import Expression
from regast.exceptions import RegastException

class UnaryOperator(Enum):
    PLUSPLUS_PRE = 0
    PLUSPLUS_POST = 1
    MINUSMINUS_PRE = 2
    MINUSMINUS_POST = 3
    BANG = 4
    TILDE = 5
    DELETE = 6
    AFTER = 7
    PLUS_PRE = 8
    MINUS_PRE = 9

    @staticmethod
    def get_operator(operator_str: str, is_postfix: bool = False):
        if operator_str == "++":
            if is_postfix:
                return UnaryOperator.PLUSPLUS_POST
            return UnaryOperator.PLUS_PRE
        elif operator_str == "--":
            if is_postfix:
                return UnaryOperator.MINUSMINUS_POST
            return UnaryOperator.MINUSMINUS_PRE
        elif operator_str == "!":
            return UnaryOperator.BANG
        elif operator_str == "~":
            return UnaryOperator.TILDE
        elif operator_str == "delete":
            return UnaryOperator.DELETE
        elif operator_str == "after":
            return UnaryOperator.AFTER
        elif operator_str == "+":
            return UnaryOperator.PLUS_PRE
        elif operator_str == "-":
            return UnaryOperator.MINUS_PRE
        
        raise RegastException(f"get_operator: Unknown unary operator: {operator_str}")

    def __str__(self):
        if self == UnaryOperator.BANG:
            return "!"
        elif self == UnaryOperator.TILDE:
            return "~"
        elif self == UnaryOperator.DELETE:
            return "delete"
        elif self == UnaryOperator.AFTER:
            return "after"
        elif self == UnaryOperator.PLUS_PRE:
            return "+"
        elif self == UnaryOperator.MINUS_PRE:
            return "-"
        elif self in [UnaryOperator.PLUSPLUS_PRE, UnaryOperator.PLUSPLUS_POST]:
            return "++"
        elif self in [UnaryOperator.MINUSMINUS_PRE, UnaryOperator.MINUSMINUS_POST]:
            return "--"
        
        raise RegastException(f"str: Unknown unary operator: {self}")

class UnaryOperation(Expression):
    def __init__(
        self,
        expression: Expression,
        operator: UnaryOperator,
    ):
        super().__init__()

        self._expression = expression
        self._operator = operator
        
    @property
    def expression(self) -> Expression:
        return self._expression
    
    @property
    def operator(self) -> UnaryOperator:
        return self._operator
    
    @property
    def is_prefix(self) -> bool:
        return self.operator not in [UnaryOperator.PLUSPLUS_POST, UnaryOperator.MINUSMINUS_POST]

    @property
    def children(self) -> List:
        return [self.expression]

    def __str__(self):
        if not self.is_prefix:
            return str(self.expression) + str(self.operator)
        
        if self.operator in [UnaryOperator.DELETE, UnaryOperator.AFTER]:
            return str(self.operator) + " " + str(self.expression)
        return str(self.operator) + str(self.expression)

    def __eq__(self, other):
        if isinstance(other, UnaryOperation):
            return self.expression == other.expression and self.operator == other.operator
        return False