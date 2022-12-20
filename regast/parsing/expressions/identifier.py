from regast.parsing.expressions.expression import Expression

class Identifier(Expression):
    def __init__(self, ctx):    # IdentifierContext
        super().__init__(ctx)
    
    @property
    def text(self):
        return self.context.getText()

    def __str__(self):
        return self.context.getText()

    def __eq__(self, other):
        if isinstance(other, str):
            return self.text == other
        return self == other