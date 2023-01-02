from typing import List

from regast.core.expressions.expression import Expression

class TupleExpression(Expression):
    def __init__(
        self, 
        expressions: List[Expression]
    ):
        super().__init__()

        self._expressions: List[Expression] = expressions

    @property
    def expressions(self) -> List[Expression]:
        return list(self._expressions)

    @property
    def children(self) -> List:
        return self.expressions

    @property
    def __str__(self):
        return "(" + ", ".join([str(x) for x in self.expressions]) + ")"
    
    @property
    def __eq__(self, other):
        if isinstance(other, TupleExpression):
            return self.expressions == other.expressions
        return False
