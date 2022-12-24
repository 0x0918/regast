from regast.parsing.context.context import Context

class Type(Context):
    def __init__(self, ctx):
        super().__init__(ctx)

    @property
    def storage_size(self):
        raise NotImplementedError(f"Unable to compute storage_size of {self.__class__.__name__}")

    @property
    def is_dynamic(self) -> bool:
        return False