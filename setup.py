#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

__all__ = []

# repo/setup.py 		(this file)
# repo/.setup/__init.py (imported by setup.py)
# repo/.setup/.*.py 	(imported by __init__.py)

# exclude .pyc, __pycache__/ (python3+)
# disable byte compiling:
# 	1) sys.dont_write_bytecode = True
# 	2) python -B setup.py
# 	3) PYTHONDONTWRITEBYTECODE=true (enviroment variable)
# MANIFEST.in:
# 	global-exclude *.py[co]
# 	exclude __pycache__/*

REPO = os.path.abspath(os.path.dirname(__file__))

setup = os.path.join(REPO, ".setup")
if os.path.exists(setup) and os.path.isdir(setup):
    sys.path.append(setup)
else:
    raise Exception("%s NOT EXISTS" % setup)

if __name__ == "__main__":
    __import__("__init__").main()
