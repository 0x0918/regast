# regast
**regast** is a static analyzer for identifying security vulnerabilities and gas optimizations in Solidity codebases.

**regast** converts the abstract syntax trees of Solidity code into Python classes, which can then be queried by detectors to identify common vulnerability patterns.

**regast** is heavily inspired by tools such as [Slither](https://github.com/crytic/slither) and [solstat](https://github.com/0xKitsune/solstat), but has the following differences:
* *No compilation:* **regast** is able to run directly without compilation, making it viable for codebases that are difficult to compile.
* *Easy to customize:* **regast** is designed for users to write and run their own custom detectors easily.

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
**regast** is built on top of [tree-sitter-python](https://github.com/tree-sitter/tree-sitter-python), which provides Python bindings for the [tree-sitter](https://tree-sitter.github.io/tree-sitter/) parsing library. The grammar for Solidity is taken from [tree-sitter-solidity](https://github.com/JoranHonig/tree-sitter-solidity).

`tree-sitter` first converts Solidity source code into multiple abstract syntax trees (AST). **regast** then converts each node in these ASTs into corresponding Python classes.

This allows individual detectors to easily identify common vulnerability patterns by querying the AST.

### Package Structure
Most of **regast**'s code are in the following directories:
* [`regast/core`](https://github.com/MiloTruck/regast/tree/main/regast/core) contains Python classes which represents parts of the AST.
* [`regast/detectors`](https://github.com/MiloTruck/regast/tree/main/regast/detectors) contains detectors which **regast** runs by default.
* [`regast/parsing`](https://github.com/MiloTruck/regast/tree/main/regast/parsing) contains the logic for parsing the AST from `tree-sitter` into Python classes. 

## Future improvements
### Adding support for [crytic-compile](https://github.com/crytic/crytic-compile)
As **regast** uses `tree-sitter-solidty`, **regast** is limited by its Solidity grammar. This causes **regast** to be unable to parse some Solidity codebases, or newer versions of Solidity. 

By adding support for parsing using [crytic-compile](https://github.com/crytic/crytic-compile), **regast** would be able to parse more Solidity codebases. However, this method does require code compilation.