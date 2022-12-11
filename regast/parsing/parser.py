import os
from antlr4 import FileStream, CommonTokenStream
from importlib.machinery import SourceFileLoader

from regast.utilities.definitions import ROOT_DIR

solidityLexer = None
solidityParser = None

class Parser:
    def __init__(self):
        solidity_antlr4_path = os.path.join(ROOT_DIR, 'build', 'solidity_antlr4')

        global solidityParser, solidityLexer
        solidityLexer = SourceFileLoader('SolidityLexer', os.path.join(solidity_antlr4_path, 'SolidityLexer.py')).load_module()
        solidityParser = SourceFileLoader('SolidityParser', os.path.join(solidity_antlr4_path, 'SolidityParser.py')).load_module()

    def parse_file(self, fname: str):
        lexer = solidityLexer.SolidityLexer(FileStream(fname))
        parser = solidityParser.SolidityParser(CommonTokenStream(lexer))
        print(parser.sourceUnit().contractDefinition()[0].identifier().getText())