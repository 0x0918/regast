from typing import List


class TreeSitterNode:
    def __init__(self, node):
        self._underlying_node = node
        self._children = []
        self._comments = []

    @property
    def type(self) -> str:
        return self._underlying_node.type

    @property
    def text(self) -> str:
        return self._underlying_node.text.decode()

    @property
    def children(self) -> List:
        return list(self._children)

    @property
    def field(self, field_name: str):
        """
        TODO
        Implement child_by_field_name, renamed to field
        """
        pass

    @property
    def comments(self) -> List:
        return list(self._comments)
