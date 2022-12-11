from antlr4 import FileStream, CommonTokenStream
from importlib import import_module

class Parser:
    def __init__(self):
        self.parser_module = import_module('regast.parsing.solidity_antlr4.SolidityParser')
        self.lexer_module = import_module('regast.parsing.solidity_antlr4.SolidityLexer')

    def parse_file(self, fname: str):
        lexer = self.lexer_module.SolidityLexer(FileStream(fname))
        parser = self.parser_module.SolidityParser(CommonTokenStream(lexer))
