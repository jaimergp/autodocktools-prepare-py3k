#!/bin/bash

tar xf MGLToolsPckgs.tar.gz
cd MGLToolsPckgs

mv AutoDockTools bhtree cMolKit mglutil MolKit PyBabel Support $PREFIX/lib/python2.7/site-packages/

BINARY_HOME=$PREFIX/bin
UTILITIES_HOME=$PREFIX/lib/python2.7/site-packages/AutoDockTools/Utilities24
ln -s $UTILITIES_HOME/prepare_ligand4.py $BINARY_HOME/prepare_ligand4.py
ln -s $UTILITIES_HOME/prepare_receptor4.py $BINARY_HOME/prepare_receptor4.py