from regast.core.expressions.expression import Expression

class Identifier(Expression):
    def __init__(self, text: str):
        super().__init__()

        self._text: str = text
    
    @property
    def text(self):
        return self._text

    def __str__(self):
        return self.text

    def __eq__(self, other):
        if isinstance(other, str):
            return self.text == other
        elif isinstance(other, Identifier):
            return self.text == other.text
        return False