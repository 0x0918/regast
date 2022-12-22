# regast
**regast** is a static analyzer for Solidity codebases.

## Installation
Prerequisites:
* Python 3.10 or above
* `pip3` installed

Clone this repository and its submodules
```sh
git clone --recurse-submodules https://github.com/MiloTruck/regast.git
cd regast
pip3 install .
# Or pip3 install -e . to edit the repo after installation
```

## Usage


## Implementation
* [ANTLR Grammar](https://github.com/solidity-parser/antlr/blob/492c7f161300fb53d7206606595e36b0d95c20c6/Solidity.g4)
* [Grammar from offical docs](https://docs.soliditylang.org/en/v0.8.17/grammar.html)


## TODO
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