# AutoDockTools (Prepare subset) for Py3k

Subset of [AutoDockTools v1.5.7](http://autodock.scripps.edu/resources/adt), tailored just to run:
- `prepare_receptor4.py`
- `prepare_ligand4.py`
- `prepare_dpf42.py`
- `prepare_gpf4.py`

This was ported by running `2to3` and then manually fixing incompatibilities, such as:

- Python 2.7's `string` module wrapper (admire the hackiness in `_py2k_string.py`)
- Inconsistent indentation (spaces vs tabs) - might have introduced one bug or two...
- Raised `"string exceptions"`
- `map(None, [...])` -> `zip_longest([...])`

# Usage
You can either run each script individually or use as python functions.

```python
from AutoDockTools.Utilities24.prepare4 import prepare_ligand4, prepare_receptor4, prepare_dpf42, prepare_gpf4
from subprocess import run

#prepare ligand and receptor
prepare_ligand4(ligand,outputfilename=outputfilename, **kwargs)
prepare_receptor4(receptor,outputfilename=outputfilename, **kwargs)

#prepare grid parameter file
prepare_gpf4(receptor_filename=receptor_filename, ligand_filename=ligand_filename, output_gpf_filename=output_gpf_filename,**kwargs)
run(f"autogrid4 -p {output_gpf_filename}")

#prepare parameter file and run AutoDock
prepare_dpf42(receptor_filename=receptor_filename, ligand_filename=ligand_filename,dpf_filename=dpf_filename, **kwargs)
command = f"autodock4 -p {dpf_filename}"

```

# Disclaimer

This has not been tested thoroughly _at all_. Results are not guaranteed to be the same as in the original distribution.
