"""
AutoDockTools-prepare-py3k
Preparation routines from ADT, ported to Python 3
"""
import sys
from setuptools import setup, find_packages

short_description = __doc__.split("\n")


try:
    with open("README.md", "r") as handle:
        long_description = handle.read()
except:
    long_description = "\n".join(short_description[2:])


setup(
    name='autodocktools-prepare',
    author='Jaime RG',
    author_email='jaime.rodriguez@charite.de',
    description=short_description[0],
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="1.5.7",
    license='MPL',
    packages=find_packages(),
    scripts=[
        'AutoDockTools/Utilities24/prepare_receptor4.py',
        'AutoDockTools/Utilities24/prepare_ligand4.py'
    ]
)
