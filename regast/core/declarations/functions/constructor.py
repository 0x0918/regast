from typing import List, Optional

from regast.core.common import StateMutability, Visibility
from regast.core.declarations.functions.function import Function, ModifierInvocation
from regast.core.statements.block import Block

class Constructor(Function):
    def __init__(
        self,
        modifiers: List[ModifierInvocation] = [],
        visibility: Optional[Visibility] = None,
        mutability: Optional[StateMutability] = None,
        body: Optional[Block] = None,
    ):
        assert visibility in [None, Visibility.INTERNAL, Visibility.PUBLIC]
        assert mutability in [None, StateMutability.PAYABLE]

        super().__init__(
            'constructor',
            modifiers=modifiers,
            visibility=visibility,
            mutability=mutability,
            body=body,
        )