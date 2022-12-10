from setuptools import setup, find_packages

setup(
    name='regast',
    version='1.0.0',
    description='A static analyzer for Solidity, built upon regex and ASTs.',
    author='MiloTruck',
    packages=find_packages(),
    install_requires=['tree-sitter'],
)