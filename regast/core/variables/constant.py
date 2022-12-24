from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.types.type import Type
from regast.core.variables.variable import Variable

class Constant(Variable):
    def __init__(
        self,
        type: Type,
        name: Identifier,
        initial_expression: Expression
    ):
        super().__init__(type, name=name, expression=initial_expression)

    def __str__(self):
        return str(self.type) + " constant " + str(self.name) + " = " + self.initial_expression