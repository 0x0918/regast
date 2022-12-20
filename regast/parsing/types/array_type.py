from typing import Optional, Tuple

from regast.parsing.expressions.expression import Expression
from regast.parsing.expressions.expression_parsing import parse_expression
from regast.parsing.types.type import Type
from regast.parsing.types.type_parsing import parse_type

class ArrayType(Type):
    def __init__(self, ctx):    # TypeNameContext
        super().__init__(ctx)

        self._type: Type = None
        self._expression: Expression = None

    @property
    def type(self) -> Type:
        if not self._type:
            self._type = parse_type(self.context.typeName())
        return self._type

    @property
    def length(self) -> Optional[Expression]:
        if not self._expression:
            self._expression = parse_expression(self.context.expression())
        return self._expression

    @property
    def is_dynamic(self) -> bool:
        return bool(self.length)

    @property
    def is_fixed(self) -> bool:
        return not bool(self.length)

    @property
    def storage_size(self) -> Tuple[int, bool]:
        return 32, True

    def __str__(self):
        if self.length:
            return str(self.type) + '[' + str(self.length) + ']'
        return str(self.type) + '[]'

    def __eq__(self, other):
        if not isinstance(other, ArrayType):
            return False
        return self._type == other.type and self.length == other.length

# TODO Implement length_value, getting the value of length. Then, add static array storage size calculation
"""
if self._length_value:
    elem_size, _ = self._type.storage_size
    return elem_size * int(str(self._length_value)), True
"""