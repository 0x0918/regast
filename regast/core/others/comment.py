class Comment:
    def __init__(self, node):
        self._text: str = node.text.decode()
    
    @property
    def text(self):
        return self._text

    def __str__(self):
        return self.text

    def __eq__(self, other):
        if isinstance(other, str):
            return self.text == other
        elif isinstance(other, Comment):
            return self.text == other.text
        return False