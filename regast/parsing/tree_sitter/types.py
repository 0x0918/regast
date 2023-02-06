class TypeParser:
    @staticmethod
    def parse_type_name(node):
        pass
    
    @staticmethod
    def parse_primitive_type(node):
        pass
    
    @staticmethod
    def parse_user_defined_type(node):
        assert node.type in ['user_defined_type', 'type_alias']
    
    @staticmethod
    def parse_mapping(node):
        pass
    
    @staticmethod
    def parse_array_type(node):
        pass
    
    @staticmethod
    def parse_function_type(node):
        pass


