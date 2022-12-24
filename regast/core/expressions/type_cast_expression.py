from regast.core.expressions.expression import Expression
from regast.core.types.elementary_type import ElementaryType

class TypeCastExpression(Expression):
    def __init__(
        self, 
        type: ElementaryType,
        expression: Expression
    ):
        super().__init__()

        self._type: ElementaryType = type
        self._expression: Expression = expression

    @property
    def type(self) -> ElementaryType:
        return self._type

    @property
    def casted_expression(self) -> Expression:
        return self._expression
    
    def __str__(self):
        return str(self.type) + "(" + str(self.casted_expression) + ")"

    def __eq__(self, other):
        if isinstance(other, TypeCastExpression):
            return self.type == other.type and self.casted_expression == other.casted_expression
        return False

