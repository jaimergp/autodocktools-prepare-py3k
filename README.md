# AutoDockTools (Prepare subset) for Py3k

Subset of [AutoDockTools v1.5.7](http://autodock.scripps.edu/resources/adt), tailored just to run:
- `prepare_receptor4.py`
- `prepare_ligand4.py`

This was ported by running `2to3` and then manually fixing incompatibilities, such as:

- Python 2.7's `string` module wrapper (admire the hackiness in `_py2k_string.py`)
- Inconsistent indentation (spaces vs tabs) - might have introduced one bug or two...
- Raised `"string exceptions"`
- `map(None, [...])` -> `zip_longest([...])`

# Disclaimer

This has not been tested thoroughly _at all_. Results are not guaranteed to be the same as in the original distribution.
