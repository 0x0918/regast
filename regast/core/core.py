from typing import List, Union


class Core:
    def __init__(self):
        self._tree_sitter_node = None 

    @property
    def tree_sitter_node(self):
        return self._tree_sitter_node

    @property
    def children(self) -> List:
        return []

    def get_instances_of(self, core_type: Union[str, type]):
        """
        Returns all children instances of a certain core type

        TODO Can this be optimized? Let's say I want to find instances of multiple core_types at the same time,
        would there be a way to only iterate once?
        """
        # Recursively get all instances of core_type
        instances = self.children + [x.get_instances_of(core_type) for x in self.children]

        # Ensure there are no duplicates (eg. VariableDeclarationStatement and LocalVariable)
        return list(set(instances))        

    def __hash__(self):
        return hash(self.tree_sitter_node)