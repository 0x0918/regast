from typing import List, Optional, Union

from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier

class StructArguments(Expression):
    def __init__(
        self,
        fields: List[Identifier] = [],
        arguments: List[Expression] = [],
    ):
        super().__init__()
    
        assert len(fields) == len(arguments)

        self._fields: List[Identifier] = fields
        self._arguments: List[Expression] = arguments

    @property
    def fields(self) -> List[Expression]:
        return list(self._fields)

    @property
    def arguments(self) -> List[Expression]:
        return list(self._arguments)
    
    def get_argument_by_field(self, field: Union[Identifier, str]) -> Optional[Expression]:
        if field in self.fields:
            return self.arguments[self.fields.index(field)]

    def __str__(self):
        return "{" + ", ".join([str(self.fields[i]) + ": " + str(self.arguments[i]) for i in range(len(self.fields))]) + "}"

    def __eq__(self, other):
        if isinstance(other, StructArguments):
            return self.fields == other.fields and self.arguments == other.arguments
        return False


class StructExpression(StructArguments):
    def __init__(
        self,
        struct_name: Expression,
        fields: List[Identifier] = [],
        arguments: List[Expression] = [],
    ):
        super().__init__(fields=fields, arguments=arguments)
    
        self._struct_name: Expression = struct_name

    @property
    def struct_name(self) -> Expression:
        return self._struct_name

    def __str__(self):
        s = str(self.struct_name) + "{"
        s += ", ".join([str(self.fields[i]) + ": " + str(self.arguments[i]) for i in range(len(self.fields))])            
        s += "}"
        return s

    def __eq__(self, other):
        if isinstance(other, StructExpression):
            return self.struct_name == other.struct_name and self.fields == other.fields and self.arguments == other.arguments
        return False
            