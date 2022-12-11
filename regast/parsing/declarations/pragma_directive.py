class Pragma:
    def __init__(self, ctx):
        self._name: str = ctx.pragmaName().getText()
        self._value: str = ctx.pragmaValue().getText()

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def value(self) -> str:
        return self._value

    @property
    def version(self) -> str:
        return self._value

    @property
    def is_solidity_version(self) -> bool:
        return self._name == "solidity"

    @property
    def is_abi_encoder_v2(self) -> bool:
        return self._name == "experimental" and self._value == "ABIEncoderV2"

    def __str__(self):
        return "pragma " + self._name + " " + self._value