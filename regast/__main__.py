#!/usr/bin/env python3

import inspect
from typing import Dict, List

from regast.detectors import all_detectors
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result
from regast.regast import Regast
from regast.utilities.command_line import handle_arguments
from regast.utilities.output import output_to_stdout
from regast.utilities.setup_dependencies import initialize_dependencies


def get_detectors():
    return [x[1] for x in inspect.getmembers(all_detectors, inspect.isclass) if issubclass(x[1], Detector)]

def get_results_from_ast(
    source_fnames: List[str], 
    files_in_scope: List[str],
    remaps: Dict[str, str],
) -> Dict[DetectorClassification, Dict[Detector, List[Result]]]:
    # Initialize regast class, which parses ast
    regast = Regast(source_fnames, files_in_scope, remaps)

    # Run detectors and filter results
    for detector in get_detectors():
        regast.register_detector(detector)

    results = regast.run_detectors()
    return results

def main():
    # Handle dependencies
    initialize_dependencies()

    # Parse arguments from command line
    args = handle_arguments()

    # Run detectors
    results = get_results_from_ast(args.contract, args.scope, args.remap)

    # Output results to stdout
    output_to_stdout(results)

if __name__ == '__main__':
    main()

"""
TODO
- [ ] Parsing of ASTs to classes
     - [ ] Scope resolution
- [ ] Implement `Result` class
- [ ] Detectors
    - [ ] Complete `detector.py`
        - [ ] Regex
        - [ ] Using classes API
        - [ ] Queries?
    - [ ] Add detectors
- [ ] Output
    - [ ] stdout
    - [ ] Markdown
        - [ ] Default behaviour from `detector.NAME` and `detector.DESCRIPTION`
        - [ ] Use `detector.TEMPLATE` if specified
- [ ] Implement importing detectors and templates from custom directories
    - [ ] Add command line option `--detectors` and `--templates`
    - [ ] Figure out how to import detectories from a custom directory
- [ ] Documentation
    - [ ] README
    - [ ] How to create a new detector/classification
        - [ ] API for individual classes
    - [ ] Included detectors
- [ ] VSCode Extension
    - [ ] Incremental parsing
        - [ ] Find a way to save the "state"
        - [ ] Only run parsing and detectors on modified parts of code
    - [ ] Linting and refactoring using detectors (eg. Gas Detectors)
    - [ ] CodeQL-like style of writing a detector and running in the editor
        - This could just be the ability to execute individual detectors using the cmdline, and passing the output to VSCode to display somehow
"""