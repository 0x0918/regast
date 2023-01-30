from typing import List, Optional
from regast.core.core import Core
from regast.core.statements.block import Block
from regast.parsing.ast_node import ASTNode

class FunctionBody(Core):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._body: Optional[Block] = None

    @property
    def body(self) -> Optional[Block]:
        return self._body

    @property
    def children(self) -> List:
        return [self.body] if self.body else []

# TODO Implement additional functionality here (eg. local variables, return statements, require statements)