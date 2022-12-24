from typing import Optional

from regast.core.variables.variable import DataLocation, Variable
from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.types.type import Type

class FunctionTypeVariable(Variable):
    def __init__(
        self, 
        type: Type,
        name: Optional[Identifier] = None,
        data_location: Optional[DataLocation] = None,
        expression: Optional[Expression] = None
    ):
        super().__init__(type, name, data_location, expression)