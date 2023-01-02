from typing import List
from regast.core.expressions.expression import Expression
from regast.core.types.type import Type

class TypeExpression(Expression):
    def __init__(
        self,
        type: Type
    ):
        super().__init__()

        self._type: Type = type

    @property
    def type(self) -> Type:
        return self._type

    @property
    def children(self) -> List:
        return self.type

    def __str__(self):
        return "type(" + str(type) + ")"

    def __eq__(self, other):
        if isinstance(other, TypeExpression):
            return self.type == other.type
        return False