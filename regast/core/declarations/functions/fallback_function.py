from typing import List, Optional

from regast.core.common import StateMutability, Visibility
from regast.core.declarations.functions.function import Function, ModifierInvocation
from regast.core.statements.block import Block
from regast.core.types.user_defined_type import UserDefinedType
from regast.core.variables.parameter import Parameter

class FallbackFunction(Function):
     def __init__(
        self,
        parameters: List[Parameter] = [],
        return_parameters: List[Parameter] = [],
        modifiers: List[ModifierInvocation] = [],
        mutability: Optional[StateMutability] = None,
        virtual: bool = False,
        overrides: List[UserDefinedType] = [],
        body: Optional[Block] = None,
    ):
        super().__init__(
            'fallback',
            parameters=parameters,
            return_parameters=return_parameters,
            visibility=Visibility.EXTERNAL,
            modifiers=modifiers,
            mutability=mutability,
            virtual=virtual,
            overrides=overrides,
            body=body
        )