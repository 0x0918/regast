from typing import List, Optional

from regast.core.core import Core
from regast.core.declarations.functions.function_body import FunctionBody
from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.expressions.struct_expression import StructArguments
from regast.core.statements.block import Block
from regast.core.types.user_defined_type import UserDefinedType
from regast.core.variables.parameter import Parameter
from regast.core.common import Visibility, StateMutability

class ModifierInvocation(Core):
    def __init__(
        self, 
        name: UserDefinedType,
        struct_arguments: Optional[StructArguments] = None,
        arguments: List[Expression] = [],
    ):
        super().__init__()

        self._name: UserDefinedType = name
        self._struct_arguments: Optional[StructArguments] = struct_arguments
        self._arguments: List[Expression] = arguments

    @property
    def name(self) -> str:
        return ".".join([str(x) for x in self.identifiers])

    @property
    def struct_arguments(self) -> Optional[StructArguments]:
        return self._struct_arguments

    @property
    def arguments(self) -> List[Expression]:
        return list(self._arguments)

class Function(FunctionBody):
    def __init__(
        self,
        name: Identifier,
        parameters: List[Parameter] = [],
        return_parameters: List[Parameter] = [],
        modifiers: List[ModifierInvocation] = [],
        visibility: Optional[Visibility] = None,
        mutability: Optional[StateMutability] = None,
        virtual: bool = False,
        overrides: List[UserDefinedType] = [],
        body: Optional[Block] = None,
    ):
        super().__init__(body=body)

        self._name: Identifier = name
        
        self._parameters: List[Parameter] = parameters
        self._return_parameters: List[Parameter] = return_parameters
        self._modifiers: List[ModifierInvocation] = modifiers

        self._visibility: Optional[Visibility] = visibility
        self._mutability: Optional[StateMutability] = mutability

        self._virtual: bool = virtual
        self._overrides: List[UserDefinedType] = overrides

    @property
    def name(self) -> Identifier:
        return self._name

    @property
    def parameters(self) -> List[Parameter]:
        return list(self._parameters)
        
    @property
    def return_parameters(self) -> List[Parameter]:
        return list(self._return_parameters)

    @property
    def modifiers(self) -> List[ModifierInvocation]:
        return list(self._modifiers)

    @property    
    def visibility(self) -> Visibility:
        if self._visibility:
            return self._visibility
        return Visibility.PUBLIC

    @property
    def declared_visibility(self) -> Optional[Visibility]:
        """
        This is used to differentiate state variables explicitly declared public
        """
        return self._visibility

    @property
    def mutability(self) -> StateMutability:
        if self._mutability:
            return self._mutability
        return StateMutability.NON_PAYABLE

    @property
    def declared_mutability(self) -> Optional[StateMutability]:
        return self._mutability

    @property
    def is_virtual(self) -> bool:
        return self._virtual

    @property
    def overrides(self) -> List[UserDefinedType]:
        return list(self._overrides)

    def __eq__(self, other):
        if isinstance(other, Function):
            return (
                self.name == other.name and 
                self.parameters == other.parameters and 
                self.return_parameters == other.return_parameters and 
                self.modifiers == other.modifiers and 
                self.visibility == other.visibility and
                self.mutability == other.mutability and
                self.is_virtual == other.is_virtual and 
                self.overrides == other.overrides
            )
        return False