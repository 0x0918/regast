from typing import List

from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier

class MemberAccess(Expression):
    def __init__(
        self,
        object: Expression,
        member: Identifier,
    ):
        super().__init__()

        self._object: Expression = object
        self._member: Identifier = member

    @property
    def object(self) -> Expression:
        return self._object

    @property
    def member(self) -> Identifier:
        return self._member

    @property
    def children(self) -> List:
        return [self.object + self.member]

    def __str__(self):
        return str(self.object) + "." + str(self.member)

    def __eq__(self, other):
        if isinstance(other, MemberAccess):
            return self.object == other.object and self.member == other.member
        return False
