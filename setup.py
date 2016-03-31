#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__ = []
import sys
from os.path import *

# __pycache__/ conflict with setuptools
sys.dont_write_bytecode = True  # REQUIRED!

repo = abspath(dirname(__file__))

# repo/setup.py 	- this file
# repo/.setup/*.py 	- python files imported by setup.py
setup = join(repo, ".setup")
if exists(setup) and isdir(setup):
    sys.path.append(setup)
else:
    raise Exception("%s NOT EXISTS" % setup)

if __name__ == "__main__":
    __import__("__setup__")
