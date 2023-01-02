from typing import List
from regast.core.expressions.expression import Expression
from regast.core.types.type import Type

class NewExpression(Expression):
    def __init__(
        self, 
        type: Type
    ):
        super().__init__()

        self._type = type

    @property
    def type(self) -> Type:
        return self._type

    @property
    def __str__(self):
        return "new " + self.type

    @property
    def children(self) -> List:
        return [self.type]
    
    @property
    def __eq__(self, other):
        if isinstance(other, NewExpression):
            return self.type == other.type
        return False
