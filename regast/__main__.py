#!/usr/bin/env python3

import argparse
import inspect
import os
import glob
from typing import Dict, List, Tuple

from regast.detectors import all_detectors
from regast.detectors.detector import Detector

def get_results_from_ast(
    detectors: List[Detector], 
    contract_paths: List[str], 
    files_in_scope: List[str]
) -> None:
    parser = initialize_parser()

def get_detectors():
    return [x[1] for x in inspect.getmembers(all_detectors, inspect.isclass) if issubclass[x[1], Detector]]

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

def parse_argument_scope(contract_paths: List[str], scope_filename: str) -> List[str]:
    if not os.path.isfile(scope_filename):
        raise Exception(f'[!] --scope: {scope_filename} does not exist.')

    with open(scope_filename, 'r') as f:
        scope_lines = f.readlines()

        if not scope_lines:
            raise Exception(f'[!] --scope: {scope_filename} is empty')

        # Match all filenames in scope with actual files
        files_in_scope = []
        for filename in scope_lines:
            filepaths = [x for x in contract_paths if os.path.abspath(x).endswith(filename)]

            if not filepaths:
                raise Exception(f'[!] --scope: {filename} does not match any file')

            if len(filepaths) > 1:
                tmp = ', '.join(filepaths)
                raise Exception(f'[!] --scope: {filename} matches more than one file: {tmp}')

            files_in_scope.append(filepaths)
        
        return files_in_scope

def parse_argument_remap(remappings_filename: str) -> Dict[str, str]:
    if not os.path.isfile(remappings_filename):
        raise Exception(f'[!] --remap: {remappings_filename} does not exist.')

    with open(remappings_filename, 'r') as f:
        remap_lines = f.readlines()

        if not remap_lines:
            raise Exception(f'[!] --remap: {remappings_filename} is empty')

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
    contract_paths = parse_argument_contract(args.contract)
    files_in_scope = parse_argument_scope(contract_paths, args.scope)
    remappings = parse_argument_remap(args.remap)

    return contract_paths, files_in_scope, remappings

def main() -> None:
    # Parse arguments from command line
    contract_paths, files_in_scope, remappings = handle_arguments()

    # Get detectors and run them
    detectors = get_detectors()
    regast, grouped_results = get_results_from_ast(detectors, contract_paths, files_in_scope)

if __name__ == '__main__':
    main()