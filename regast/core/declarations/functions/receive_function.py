from typing import List, Optional

from regast.core.common import StateMutability, Visibility
from regast.core.declarations.functions.function import Function, ModifierInvocation
from regast.core.statements.block import Block
from regast.core.types.user_defined_type import UserDefinedType

class ReceiveFunction(Function):
    def __init__(
        self,
        modifiers: List[ModifierInvocation] = [],
        virtual: bool = False,
        overrides: List[UserDefinedType] = [],
        body: Optional[Block] = None,
    ):
        super().__init__(
            'receive',
            visibility=Visibility.EXTERNAL,
            mutability=StateMutability.PAYABLE,
            modifiers=modifiers,
            virtual=virtual,
            overrides=overrides,
            body=body,
        )