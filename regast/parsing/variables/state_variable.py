from regast.parsing.tokens import StateVariableMutability, StateVariableVisibility
from regast.parsing.variables.variable import Variable


class StateVariable(Variable):
    def __init__(self, ctx):    # StateVariableDeclarationContext
        super().__init__(ctx)

        self._mutability: StateVariableMutability = None
        self._visibility: StateVariableVisibility = None

# TODO To complete