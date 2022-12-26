from typing import List, Optional

from regast.core.declarations.functions.function import Function
from regast.core.expressions.identifier import Identifier
from regast.core.statements.block import Block
from regast.core.types.user_defined_type import UserDefinedType
from regast.core.variables.parameter import Parameter

class Modifier(Function):
    def __init__(
        self,
        name: Identifier,
        parameters: List[Parameter] = [],
        virtual: bool = False,
        overrides: List[UserDefinedType] = [],
        body: Optional[Block] = None
    ):
        super().__init__(
            name=name,
            parameters=parameters,
            virtual=virtual,
            overrides=overrides,
            body=body
        )