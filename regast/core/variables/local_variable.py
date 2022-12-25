from typing import List, Optional

from regast.core.core import Core
from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.types.type import Type
from regast.core.variables.variable import DataLocation, Variable

class LocalVariable(Variable):
    def __init__(
        self,
        type: Type,
        name: Identifier,
        data_location: Optional[DataLocation] = None,
        initial_expression: Optional[Expression] = None,
    ):
        super().__init__(
            type,
            name=name,
            data_location=data_location,
            expression=initial_expression
        )