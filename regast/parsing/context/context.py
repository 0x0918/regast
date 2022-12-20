class Context:
    def __init__(self, ctx):
        self._context = ctx

    @property
    def context(self):
        return self._context