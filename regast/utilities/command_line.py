import argparse
import os
import glob
from typing import Dict, List, Tuple

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
        
def handle_arguments() -> Tuple[List[str], List[str], Dict[str, str]]:
    parser = argparse.ArgumentParser(description='Scan for vulnerabilities based on regex or AST queries.')
    parser.add_argument('contract', metavar='<contract>', type=str,
                        help='Soldiity file or folder to scan')
    parser.add_argument('--scope', metavar='<scope.txt>', type=str,
                        help='Text file containing a list of contracts in scope')
    parser.add_argument('--remap', metavar='<remappings.txt>', type=str,
                        help='Text file containing import remappings')

    args = parser.parse_args()
    contract_fnames = parse_argument_contract(args.contract)

    files_in_scope = None
    if args.scope is not None:
        files_in_scope = parse_argument_scope(contract_fnames, args.scope)
        
    remappings = None
    if args.remap is not None:
        remappings = parse_argument_remap(args.remap)

    return contract_fnames, files_in_scope, remappings