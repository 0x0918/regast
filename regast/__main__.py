#!/usr/bin/env python3

import importlib.util as import_util
import inspect
from typing import Dict, List

from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result
from regast.regast import Regast
from regast.utilities.command_line import handle_arguments
from regast.utilities.output import output_to_stdout
from regast.utilities.setup_dependencies import initialize_dependencies


def get_detectors(detector_paths: List[str]) -> List[Detector]:
    detectors = []

    for detector_path in detector_paths:
        # Dynamically load module from Python file path
        spec = import_util.spec_from_file_location('all_detectors', detector_path)
        module = import_util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Get detectors from loaded module
        for detector_class in inspect.getmembers(module, inspect.isclass):
            if issubclass(detector_class[1], Detector) and detector_class[1] != Detector:
                detectors.append(detector_class[1])

    return detectors

def get_results_from_ast(args) -> Dict[DetectorClassification, Dict[Detector, List[Result]]]:
    # Initialize regast class, which parses ast
    regast = Regast(args.contract, args.scope)

    # Run detectors and filter results
    for detector in get_detectors(args.detectors):
        regast.register_detector(detector)

    results = regast.run_detectors()
    return results

def main():
    # Handle dependencies
    initialize_dependencies()

    # Parse arguments from command line
    args = handle_arguments()

    # Run detectors
    results = get_results_from_ast(args)

    # Output results to stdout
    output_to_stdout(results)

if __name__ == '__main__':
    main()

"""
TODO
- [ ] Scope resolution
- [ ] Name resolution
- [ ] Type resolution
- [ ] Detectors
    - [ ] Add 4naly3er remaining detectors
    - [ ] Add solstat detectors
    - [ ] Write tests for detectors
- [ ] Output
    - [ ] Markdown
        - [ ] Default behaviour from `detector.NAME` and `detector.DESCRIPTION`
- [ ] Documentation
    - [ ] Include sample reports
    - [ ] How to create a new detector/classification
        - [ ] Methods of detector class
        - [ ] example_regex_detector
        - [ ] API for individual classes
- [ ] VSCode Extension
    - [ ] Incremental parsing
        - [ ] Find a way to save the "state"
        - [ ] Only run parsing and detectors on modified parts of code
    - [ ] Linting and refactoring using detectors (eg. Gas Detectors)
    - [ ] CodeQL-like style of writing a detector and running in the editor
        - This could just be the ability to execute individual detectors using the cmdline, and passing the output to VSCode to display somehow
"""