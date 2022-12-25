from typing import List, Optional
from regast.core.expressions.expression import Expression
from regast.core.expressions.struct_expression import StructArguments

class CallExpression(Expression):
    def __init__(
        self,
        called: Expression,
        struct_arguments: Optional[StructArguments] = None,
        arguments: List[Expression] = [],
    ):
        super().__init__()
    
        self._called: Expression = called
        self._struct_arguments: Optional[StructArguments] = struct_arguments
        self._arguments: List[Expression] = arguments

    @property
    def called(self) -> Expression:
        return self._called

    @property
    def struct_arguments(self) -> Optional[StructArguments]:
        return self._struct_arguments

    @property
    def arguments(self) -> List[Expression]:
        return list(self._arguments)

    @property
    def gas(self) -> Optional[Expression]:
        if self.struct_arguments and "gas" in self.struct_arguments.fields:
            return self.struct_arguments.get_argument_by_field("gas")

    @property
    def value(self) -> Optional[Expression]:
        if self.struct_arguments and "value" in self.struct_arguments.fields:
            return self.struct_arguments.get_argument_by_field("value")

    @property
    def salt(self) -> Optional[Expression]:
        if self.struct_arguments and "salt" in self.struct_arguments.fields:
            return self.struct_arguments.get_argument_by_field("salt")

    def __str__(self):
        s = str(self.called)
        if self.struct_arguments:
            s += str(self.struct_arguments)
        s += "(" + ", ".join([str(x) for x in self.arguments]) + ")"
        return s

    def __eq__(self, other):
        if isinstance(other, CallExpression):
            return self.called == other.called and self.struct_arguments == other.struct_arguments and self.arguments == other.arguments 
        return False
            