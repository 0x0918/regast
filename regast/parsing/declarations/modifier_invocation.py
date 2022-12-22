from typing import List

from regast.parsing.context.context import Context
from regast.parsing.expressions.expression import Expression
from regast.parsing.expressions.expression_parsing import parse_expression
from regast.parsing.expressions.identifier import Identifier

class ModifierInvocation(Context):
    def __init__(self, ctx):
        super().__init__(ctx)

        self._identifier: Identifier = None
        self._expressions: List[Expression] = []

    @property
    def name(self) -> Identifier:
        if not self._identifier:
            self._identifier = Identifier(self.context.identifier())
        return self._identifier

    @property
    def arguments(self) -> List[Expression]:
        if not self._expressions:
            expressions = self.context.expressionList().expression
            self._expressions = [parse_expression(x) for x in expressions]
        return list(self._expressions)                