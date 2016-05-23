#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

__all__ = []

# __pycache__/ conflict with setuptools
sys.dont_write_bytecode = True  # REQUIRED!

repo = os.path.abspath(os.path.dirname(__file__))

# repo/setup.py 	- this file
# repo/.setup/*.py 	- python files imported by setup.py
setup = os.path.join(repo, ".setup")
if os.path.exists(setup) and os.path.isdir(setup):
    sys.path.append(setup)
else:
    raise Exception("%s NOT EXISTS" % setup)

if __name__ == "__main__":
    __import__("__init__").main()
