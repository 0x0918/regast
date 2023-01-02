from typing import List

from regast.core.core import Core
from regast.core.declarations.contracts.contract import Contract
from regast.core.declarations.custom_error import CustomError
from regast.core.declarations.directives.using_directive import UsingDirective
from regast.core.declarations.enum import Enum
from regast.core.declarations.functions.function import Function
from regast.core.declarations.directives.import_directive import Import
from regast.core.declarations.directives.pragma_directive import Pragma
from regast.core.declarations.struct import Struct
from regast.core.declarations.type_definition import TypeDefinition
from regast.core.variables.constant import Constant

class SourceUnit(Core):
    def __init__(
        self,
        pragma_directives: List[Pragma] = [],
        import_directives: List[Import] = [],
        contracts: List[Contract] = [],
        enums: List[Enum] = [],
        structs: List[Struct] = [],
        functions: List[Function] = [],
        constants: List[Constant] = [],
        custom_errors: List[CustomError] = [],
        using_directives: List[UsingDirective] = [],
        type_definitions: List[TypeDefinition] = []
    ):
        super().__init__()

        self._pragma_directives: List[Pragma] = pragma_directives
        self._import_directives: List[Import] = import_directives
        self._using_directives: List[UsingDirective] = using_directives
        self._contracts: List[Contract] = contracts
        self._enums: List[Enum] = enums
        self._structs: List[Struct] = structs
        self._functions: List[Function] = functions
        self._constants: List[Constant] = constants
        self._custom_errors: List[CustomError] = custom_errors
        self._type_definitions: List[TypeDefinition ] = type_definitions

    @property
    def pragma_directives(self) -> List[Pragma]:
        return list(self._pragma_directives)

    @property
    def using_directives(self) -> List[UsingDirective]:
        return list(self._using_directives)

    @property
    def import_directives(self) -> List[Import]:
        return list(self._import_directives)

    @property
    def contracts(self) -> List[Contract]:
        return list(self._contracts)

    @property
    def enums(self) -> List[Enum]:
        return list(self._enums)

    @property
    def structs(self) -> List[Struct]:
        return list(self._structs)

    @property
    def functions(self) -> List[Function]:
        return list(self._functions)

    @property
    def constants(self) -> List[Constant]:
        return list(self._constants)

    @property
    def custom_errors(self) -> List[CustomError]:
        return list(self._custom_errors)

    @property
    def type_definitions(self) -> List[TypeDefinition]:
        return list(self._type_definitions)

    def __eq__(self, other):
        if isinstance(other, SourceUnit):
            return (
                self.pragma_directives == other.pragma_directives and
                self.import_directives == other.import_directives and
                self.using_directives == other.using_directives and
                self.contracts == other.contracts and
                self.enums == other.enums and
                self.structs == other.structs and
                self.functions == other.functions and
                self.constants == other.constants and
                self.custom_errors == other.custom_errors and
                self.type_definitions == other.type_definitions
            )
        return False