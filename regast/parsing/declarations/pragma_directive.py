from regast.parsing.context.context import Context
from regast.parsing.expressions.identifier import Identifier

class Pragma(Context):
    def __init__(self, ctx):    # PragmaDirectiveContext
        super().__init__(ctx)
        
        self._name: Identifier = None
        self._value: str = None

    @property
    def name(self) -> str:
        if not self._name:
            self._name = Identifier(self.context.pragmaName().identifier())
        return self._name
    
    @property
    def value(self) -> str:
        if not self._value:
            self._value = self.context.pragmaValue().getText()
        return self._value

    @property
    def version(self) -> str:
        return self.value

    @property
    def is_solidity_version(self) -> bool:
        return self.name == "solidity"

    @property
    def is_abi_encoder_v2(self) -> bool:
        return self.name == "experimental" and self.value == "ABIEncoderV2"

    def __str__(self):
        return "pragma " + str(self.name) + " " + self.value