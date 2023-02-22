# regast
**regast** is a static analyzer for identifying security vulnerabilities and gas optimizations in Solidity codebases.

**regast** converts the abstract syntax trees of Solidity code into Python classes, which can then be queried by detectors to identify common vulnerability patterns.

**regast** is heavily inspired by tools such as [Slither](https://github.com/crytic/slither), [4naly3er](https://github.com/Picodes/4naly3er) and [solstat](https://github.com/0xKitsune/solstat), but has the following differences:
* *No compilation:* **regast** is able to run directly without compilation, making it viable for codebases that are difficult to compile.
* *Easy to customize:* **regast** is designed for users to easily write and run their own custom detectors.

## Table of Contents
- [regast](#regast)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
    - [Installation](#installation)
    - [Running **regast**](#running-regast)
  - [Detectors](#detectors)
    - [Included detectors](#included-detectors)
    - [Writing custom detectors](#writing-custom-detectors)
  - [Implementation](#implementation)
    - [Repository structure](#repository-structure)
    - [Future improvements](#future-improvements)


## Usage

### Installation
**regast** requires Python 3.10 or above.

First, clone this repository and its submodules:
```sh
git clone --recurse-submodules https://github.com/MiloTruck/regast.git
cd regast
```

Install **regast** using either `pip` or `setuptools`:
```sh
# Using pip
pip3 install .

# Using setuptools
python3 setup.py install
```

After installation, the repository can be deleted:
```sh
cd ..
rm -r regast
```

### Running **regast**
The `regast` command can be used on either `.sol` file or a folder containing Solidity files:
```sh
$ regast --help
usage: regast [-h] [-s <scope.txt>] [-d <path_to_detector>] <path_to_contract>

Scan for vulnerabilities based on regex or AST queries.

positional arguments:
  <path_to_contract>    Path to .sol file or folder containing .sol files to scan

options:
  -h, --help            show this help message and exit
  -s <scope.txt>, --scope <scope.txt>
                        Text file containing a list of contracts in scope
  -d <path_to_detector>, --detectors <path_to_detector>
                        Path to .py file or folder containing .py files which implement detectors
```

## Detectors

### Included detectors
Below are the currently implemented detectors which **regast** runs by default. Most of the detectors from [4naly3er](https://github.com/Picodes/4naly3er) and [solstat](https://github.com/0xKitsune/solstat) will be included in the future.

| Detector                                                                         | Description                                                               | Classification |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | -------------- |
| [`address_balance`](regast/detectors/gas/address_balance.py)                     | Use `selfbalance()` instead of `address(this).balance`.                   | Gas            |
| [`address_zero`](regast/detectors/gas/address_zero.py)                           | Use assembly to check for `address(0)`.                                   | Gas            |
| [`assign_update_array_value`](regast/detectors/gas/assign_update_array_value.py) | Update array values using `arr[i] += n` instead of `arr[i] = arr[i] + n`. | Gas            |
| [`bool_storage`](regast/detectors/gas/bool_storage.py)                           | Using `bool` for storage incurs overhead.                                 | Gas            |
| [`cache_array_length`](regast/detectors/gas/cache_array_length.py)               | Cache array length outside of for-loops.                                  | Gas            |
| [`custom_error`](regast/detectors/gas/custom_error.py)                           | Use custom errors instead of `require` statements.                        | Gas            |
| [`initialize_default_value`](regast/detectors/gas/initialize_default_value.py)   | Unnecessary initialization of variables with default values               | Gas            |
| [`long_revert_string`](regast/detectors/gas/long_revert_string.py)               | `require` statements with long error messages.                            | Gas            |
| [`post_increment`](regast/detectors/gas/post_increment.py)                       | `++i` costs less gas than `i++` or `i += 1`.                              | Gas            |
| [`private_constant`](regast/detectors/gas/private_constant.py)                   | Declare constants as `private` instead of non-public to save gas.         | Gas            |
| [`shift_arithmetic`](regast/detectors/gas/shift_arithmetic.py)                   | Use `<<` and `>>` instead of multiplication/division where possible.      | Gas            |
| [`split_require_statements`](regast/detectors/gas/split_require_statements.py)   | Use separate `require` statements instead of `&&`.                        | Gas            |
| [`unsigned_comparison`](regast/detectors/gas/unsigned_comparison.py)             | Use `!= 0` instead of `> 0` for unsigned integer comparison.              | Gas            |

### Writing custom detectors

For information on how to write custom detectors, refer to [`docs/writing-custom-detectors.md`](docs/writing-custom-detectors.md).

## Implementation
**regast** is built on top of [tree-sitter-python](https://github.com/tree-sitter/tree-sitter-python), which provides Python bindings for the [tree-sitter](https://tree-sitter.github.io/tree-sitter/) parsing library. The grammar for Solidity is taken from [tree-sitter-solidity](https://github.com/JoranHonig/tree-sitter-solidity).

`tree-sitter` first converts Solidity source code into multiple abstract syntax trees (AST). **regast** then converts each node in these ASTs into corresponding Python classes.

This allows individual detectors to easily identify common vulnerability patterns by querying the AST.

### Repository structure
Most of **regast**'s code are in the following directories:
* [`regast/core`](regast/core) contains Python classes which represents parts of the AST.
* [`regast/detectors`](regast/detectors) contains detectors which **regast** runs by default.
* [`regast/parsing`](regast/parsing) contains the logic for parsing the AST from `tree-sitter` into Python classes. 

### Future improvements
*  **Adding support for [crytic-compile](https://github.com/crytic/crytic-compile)**  
**regast** is limited by the Solidity grammar defined in  `tree-sitter-solidity`, which is not updated frequently. This causes **regast** to be unable to parse some Solidity codebases, or newer versions of Solidity. <br> By adding support for parsing using [crytic-compile](https://github.com/crytic/crytic-compile), **regast** would be able to parse more Solidity codebases. However, this method does require code compilation.