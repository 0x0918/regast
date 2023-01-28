"""
No throw statement
"""

class StatementParser:
    @staticmethod    
    def parse_block_statement(node):
        assert node.type in ['function_body', 'block_statement']

    @staticmethod    
    def parse_expression_statement(node):
        pass

    @staticmethod    
    def parse_variable_declaration_statement(node):
        pass

    @staticmethod    
    def parse_if_statement(node):
        pass

    @staticmethod    
    def parse_for_statement(node):
        pass

    @staticmethod    
    def parse_while_statement(node):
        pass

    @staticmethod    
    def parse_do_while_statement(node):
        pass

    @staticmethod    
    def parse_continue_statement(node):
        pass

    @staticmethod    
    def parse_break_statement(node):
        pass

    @staticmethod    
    def parse_try_statement(node):
        pass

    @staticmethod    
    def parse_return_statement(node):
        pass

    @staticmethod    
    def parse_emit_statement(node):
        pass

    @staticmethod    
    def parse_assembly_statement(node):
        pass

    @staticmethod    
    def parse_revert_statement(node):
        pass

