from regast.core.core import Core
from regast.core.expressions.identifier import Identifier

class Pragma(Core):
    def __init__(
        self,
        name: Identifier,
        value: str
    ):
        super().__init__()
        
        self._name: Identifier = name
        self._value: str = value

    @property
    def name(self) -> Identifier:
        return self._name
    
    @property
    def value(self) -> str:
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

    def __eq__(self, other):
        if isinstance(other, Pragma):
            return self.name == other.name and self.value == other.value
        return False