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

    def get_instances_of(self, *core_types: List[Union[str, type]]) -> Union[List, List[List]]:
        """
        Returns all child instances of core types specified
        - Each core type can either be a class or str (LocalVariable, "LocalVariable")
        - If only 1 core type is provided, returns a single list
        - If multiple core types are provided, returns a list of lists in the same order

        Examples:
        local_variables = a.get_instances_of(LocalVariable)
        local_variables, state_variables = a.get_instances_of(LocalVariable, "StateVariable")
        """
        instances = [[] for _ in range(len(core_types))]
        
        for child in self.children:
            # Check if child matches any of the core types
            for i in range(len(core_types)):
                core_type = core_types[i]
                if child.__class__.__name__ == str(core_type) or isinstance(child, core_type):
                    instances[i].append(child)
            
            # Recursively do this for children too, and add the results to our current ones
            child_instances = child.get_instances_of(*core_types)
            if len(core_types) == 1:            
                child_instances = [child_instances]
            instances = [instances[x] + child_instances[x] for x in range(len(core_types))]
        
        # Remove duplicates
        instances = [list(set(x)) for x in instances]         

        # Return a single list if only one core type is specified
        return instances[0] if len(core_types) == 1 else instances

    def __hash__(self):
        return hash(self.tree_sitter_node)