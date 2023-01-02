import argparse
import glob
import os
from typing import Dict, List

from regast.parsing.parser_type import ParserType


def parse_argument_contract(contract_path: str) -> List[str]:
    if not os.path.exists(contract_path):
        raise Exception(f'[!] File or directory {contract_path} does not exist.')

    if os.path.isdir(contract_path):
        files = glob.glob('**/*.sol', recursive=True)
        if not files:
            raise Exception(f'[!] Directory {contract_path} is empty.')
        return files
    else:
        return [contract_path]

def parse_argument_scope(contract_fnames: List[str], scope_fname: str) -> List[str]:
    if not os.path.isfile(scope_fname):
        raise Exception(f'[!] --scope: {scope_fname} does not exist.')

    with open(scope_fname, 'r') as f:
        scope_lines = f.readlines()

        if not scope_lines:
            raise Exception(f'[!] --scope: {scope_fname} is empty')

        # Match all fnames in scope with actual files
        files_in_scope = []
        for fname in scope_lines:
            filepaths = [x for x in contract_fnames if os.path.abspath(x).endswith(fname)]

            if not filepaths:
                raise Exception(f'[!] --scope: {fname} does not match any file')

            if len(filepaths) > 1:
                tmp = ', '.join(filepaths)
                raise Exception(f'[!] --scope: {fname} matches more than one file: {tmp}')

            files_in_scope.append(filepaths)
        
        return files_in_scope

def parse_argument_remap(remappings_fname: str) -> Dict[str, str]:
    if not os.path.isfile(remappings_fname):
        raise Exception(f'[!] --remap: {remappings_fname} does not exist.')

    with open(remappings_fname, 'r') as f:
        remap_lines = f.readlines()

        if not remap_lines:
            raise Exception(f'[!] --remap: {remappings_fname} is empty')

        remappings = {}
        for line in remap_lines:
            identifier, path = line.split('=')
            remappings[identifier] = path

        return remappings

def parse_argument_parser(parser_type_str: str) -> ParserType:
    if not parser_type_str:
        return ParserType.TREE_SITTER

    if parser_type_str not in [x.value for x in ParserType]:
        raise Exception(f'--parser: {parser_type_str} is not a valid parser')
    
    return ParserType(parser_type_str)

def handle_arguments():
    parser = argparse.ArgumentParser(description='Scan for vulnerabilities based on regex or AST queries.')
    parser.add_argument(
        'contract', 
        metavar='<contract>', 
        type=str,
        help='Soldiity file or folder to scan'
    )
    parser.add_argument(
        '--scope', 
        metavar='<scope.txt>', 
        type=str,
        help='Text file containing a list of contracts in scope'
    )
    parser.add_argument(
        '--remap', 
        metavar='<remappings.txt>', 
        type=str,
        help='Text file containing import remappings'
    )
    parser.add_argument(
        '--parser', 
        metavar='<' + ', '.join([x.value for x in ParserType]) + '>', 
        type=str,
        help='Specifies the parser to use'
    )

    args = parser.parse_args()
    args.contract = parse_argument_contract(args.contract)
    args.parser = parse_argument_parser(args.parser)

    if args.scope is not None:
        args.scope = parse_argument_scope(args.contract, args.scope)
        
    if args.remap is not None:
        args.scope = parse_argument_remap(args.remap)

    return args