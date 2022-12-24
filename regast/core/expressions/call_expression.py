from typing import List, Optional
from regast.core.expressions.expression import Expression

class CallExpression(Expression):
    def __init__(
        self,
        called: Expression,
        arguments: List[Expression] = [],
        gas: Optional[Expression] = None,
        value: Optional[Expression] = None,
        salt: Optional[Expression] = None,

    ):
        super().__init__()
    
        self._called: Expression = called
        self._arguments: List[Expression] = arguments

        self._gas: Optional[Expression] = gas
        self._value: Optional[Expression] = value
        self._salt: Optional[Expression] = salt

    @property
    def called(self) -> Expression:
        return self._called

    @property
    def arguments(self) -> List[Expression]:
        return list(self._arguments)

    @property
    def gas(self) -> Optional[Expression]:
        return self._gas

    @property
    def value(self) -> Optional[Expression]:
        return self._value

    @property
    def salt(self) -> Optional[Expression]:
        return self._salt

    def __str__(self):
        s = str(self.called)
        if self.gas or self.value or self.salt:
            gas = f"gas: {str(self.gas)}" if self.gas else ""
            value = f"value: {str(self.value)}" if self.value else ""
            salt = f"salt: {str(self.salt)}" if self.salt else ""

            s += "{" + ", ".join([x for x in [gas, value, salt] if x]) + "}"
        s += "(" + ", ".join([str(x) for x in self.arguments]) + ")"
        return s

    def __eq__(self, other):
        if isinstance(other, CallExpression):
            return self.called == other.called and self.arguments == other.arguments and self.gas == other.gas and self.value == other.value and self.salt == other.salt
        return False
            