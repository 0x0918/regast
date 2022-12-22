from typing import List, Tuple
from regast.exceptions import ParsingError

from regast.parsing.tokens import StateMutability, Visibility
from regast.parsing.types.type import Type
from regast.parsing.variables.function_type_variable import FunctionTypeVariable

class FunctionType(Type):
    def __init__(self, ctx):    # FunctionTypeNameContext
        super().__init__(ctx)

        self._visibility: Visibility = None
        self._state_mutability: StateMutability = None
        self._parameters: List[FunctionTypeVariable] = []
        self._return_parameters: List[FunctionTypeVariable] = []

        raise NotImplementedError(f'{self.__class__} not implemented.')

    @property
    def parameters(self) -> List[FunctionTypeVariable]:
        if not self._parameters:
            functionTypeParameterList = self.context.functionTypeParameterList()[0]
            self._parameters = [FunctionTypeVariable(x) for x in functionTypeParameterList.functionTypeParameter()]
        return list(self._parameters)

    @property
    def return_parameters(self) -> List[FunctionTypeVariable]:
        if not self._return_parameters:
            functionTypeParameterList = self.context.functionTypeParameterList()[1]
            self.return_parameters = [FunctionTypeVariable(x) for x in functionTypeParameterList.functionTypeParameter()]
        return list(self.return_parameters)

    @property
    def visibility(self) -> Visibility:
        if not self._visibility:
            internal = self.context.InternalKeyword()
            external = self.context.ExternalKeyword()

            if len(internal) + len(external) > 1:
                raise ParsingError(f'Failed to parse {self.context.getText()} to {self.__class__}')
                
            if internal:
                self._visibility = Visibility.INTERNAL
            elif external:
                self._visibility = Visibility.EXTERNAL
        return None

    @property                
    def state_mutability(self) -> StateMutability:
        if not self._state_mutability:
            state_mutability = self.context.stateMutability()
            
            if len(state_mutability) > 1:
                raise ParsingError(f'Failed to parse {self.context.getText()} to {self.__class__}')

            if state_mutability:
                self._state_mutability = StateMutability(state_mutability[0].getText())
        return self._state_mutability

    @property
    def storage_size(self) -> Tuple[int, bool]:
        return 24, False

    def __str__(self):
        s = 'function'
        if self.parameters:
            s += ' (' + ', '.join([str(x) for x in self.parameters]) + ')'
        if self.visibility:
            s += ' ' + self.visibility.value
        if self.state_mutability:
            s += ' ' + self.state_mutability.value
        if self.return_parameters:
            s += ' (' + ', '.join([str(x) for x in self.return_parameters]) + ')'
        return s

    def __eq__(self, other):
        if isinstance(other, FunctionType):
            return self.parameters == other.parameters and self.return_parameters == other.return_parameters and self.visibility == other.visibility and other.state_mutability == other.state_mutability
        return False
        