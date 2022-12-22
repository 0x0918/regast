from regast.parsing.tokens import Visibility, StateVariableMutability
from regast.parsing.variables.variable import Variable


class StateVariable(Variable):
    def __init__(self, ctx):    # StateVariableDeclarationContext
        super().__init__(ctx)

        self._mutability: StateVariableMutability = None
        self._visibility: Visibility = None

# TODO To complete