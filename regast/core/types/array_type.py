from typing import Optional, Tuple

from regast.core.types.type import Type
from regast.core.expressions.expression import Expression

class ArrayType(Type):
    def __init__(
        self,
        type: Type,
        expression: Optional[Expression] = None
    ):
        super().__init__()

        self._type: Type = type
        self._expression: Optional[Expression] = expression
        
    @property
    def type(self) -> Type:
        return self._type

    @property
    def length(self) -> Optional[Expression]:
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
        if isinstance(other, ArrayType):
            return self.type == other.type and self.length == other.length
        return False

# TODO Implement length_value, getting the value of length. Then, add static array storage size calculation
"""
if self._length_value:
    elem_size, _ = self._type.storage_size
    return elem_size * int(str(self._length_value)), True
"""