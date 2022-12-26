from typing import Optional
from regast.core.core import Core
from regast.core.statements.block import Block

class FunctionBody(Core):
    def __init__(self, body: Optional[Block] = None):
        super().__init__()

        self._body: Optional[Block] = body

    @property
    def body(self) -> Optional[Block]:
        return self._body

# TODO Implement additional functionality here (eg. local variables, return statements, require statements)