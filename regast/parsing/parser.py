import os
from antlr4 import FileStream, CommonTokenStream
from importlib.machinery import SourceFileLoader

from regast.utilities.definitions import ROOT_DIR
from regast.parsing.source_unit import SourceUnit

solidityLexer = None
solidityParser = None

def load_antlr4_modules():
    global solidityParser, solidityLexer
    solidity_antlr4_path = os.path.join(ROOT_DIR, 'build', 'solidity_antlr4')
    solidityLexer = SourceFileLoader('SolidityLexer', os.path.join(solidity_antlr4_path, 'SolidityLexer.py')).load_module()
    solidityParser = SourceFileLoader('SolidityParser', os.path.join(solidity_antlr4_path, 'SolidityParser.py')).load_module()

class Parser:
    def __init__(self):
        self.fname_to_sourceUnit = {}

        load_antlr4_modules()
        
    def parse_file(self, fname: str):
        lexer = solidityLexer.SolidityLexer(FileStream(fname))
        parser = solidityParser.SolidityParser(CommonTokenStream(lexer))

        self.fname_to_sourceUnit[fname] = SourceUnit(parser.sourceUnit())