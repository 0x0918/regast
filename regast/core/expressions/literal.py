from enum import Enum
from typing import Optional, Union

from regast.core.expressions.expression import Expression
from regast.utilities.math import convert_string_to_fraction, convert_subdenomination

class LiteralType(Enum):
    BOOLEAN = 0
    NUMBER = 1
    HEX = 2
    STRING = 3

class Literal(Expression):
    def __init__(
        self, 
        underlying_value: str,
        literal_type: LiteralType,
        subdenomination: Optional[str] = None
    ):
        """
        Using "2 ether" as an example:
        - underlying_value = "2"
        - literal_type = LiteralType.NUMBER
        - subdenomination = "ether"
        - value = 2000000000000000000
        """

        super().__init__()

        if literal_type == LiteralType.BOOLEAN:
            assert underlying_value in ["true", "false"]

        if literal_type not in [LiteralType.NUMBER, LiteralType.HEX]:
            assert subdenomination is None

        self._underlying_value: str = underlying_value
        self._literal_type: LiteralType = literal_type
        self._subdenomination: Optional[str] = subdenomination

    @property
    def literal_type(self) -> LiteralType:
        return self._literal_type

    @property
    def value(self) -> Union[str, bool , int]:
        if self.literal_type == LiteralType.STRING:
            return self._underlying_value
        elif self.literal_type == LiteralType.BOOLEAN:
            return self._underlying_value == "true"
        
        if self._subdenomination:
            return convert_subdenomination(self._underlying_value, self._subdenomination)
        
        return int(convert_string_to_fraction(self._underlying_value))

    def __str__(self):
        s = self._underlying_value 
        if self._subdenomination:
            s += " " + self._subdenomination
        return s

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        elif isinstance(other, bool) and self.literal_type == LiteralType.BOOLEAN:
            return self.value == other
        elif isinstance(other, int) and self.literal_type in [LiteralType.NUMBER, LiteralType.HEX]:
            return self.value == other 
        elif isinstance(other, Literal):
            return self.value == other.value
        return False




    