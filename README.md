# regast
**regast** is a static analyzer for identifying security vulnerabilities and gas optimizations in Solidity codebases.

**regast** parses the abstract syntax trees of Solidity code into Python classes, which can then be used to write detectors for common vulnerability patterns.

**regast** is heavily inspired by tools such as [Slither](https://github.com/crytic/slither) and [solstat](https://github.com/0xKitsune/solstat), but has the following differences:
* **No compilation:** 
* **Easily customizable:**

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

### Running **regast**
The `regast` command can be used on either `.sol` file or a folder containing Solidity files:
```sh
$ regast --help
usage: regast [-h] [--scope <scope.txt>] [--remap <remappings.txt>] <contract>

Scan for vulnerabilities based on regex or AST queries.

positional arguments:
  <contract>            Soldiity file or folder to scan

options:
  -h, --help            show this help message and exit
  --scope <scope.txt>   Text file containing a list of contracts in scope
  --remap <remappings.txt>
                        Text file containing import remappings
```

### Detectors
By default, **regast** runs all included detectors listed [here]().

Using the `--detectors` option, **regast** is also able to run custom-written detectors:
```sh
$ regast --detectors <detector> .
```

More details about writing your own detector can be found [here]().

## Implementation