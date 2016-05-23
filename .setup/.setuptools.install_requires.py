#!/usr/bin/env python
# setuptools setup(...,install_requires=[]) keyword
# checks that the requirements installed
# raise exception if requirements not installed:
# error: Could not find required distribution <name>
# fix - install requirements.txt first:
# 1) pip install -U <name>
# 2) pip install -r requirements.txt; python install setup.py
import os
from __init__ import REPO, readlines

__all__ = ["install_requires"]

filenames = ["requirements.txt", "requires.txt", "install_requires.txt"]
for filename in filenames:
    path = os.path.join(REPO, filename)
    if os.path.exists(path):
        install_requires = readlines(path)
        if install_requires:
            break

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
