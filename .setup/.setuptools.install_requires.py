#!/usr/bin/env python
# checks requirements BEFORE install (python install setup.py)
#
# ERRORS (depends on setiptools version):
# a) error: Could not find required distribution <name>
# b) SandboxViolation: open('name.egg-info/dependency_links.txt', 'wb') {}
#
# fix:
# pip install -r requirements.txt (REQUIRED)
# python install setup.py

import os
from __init__ import REPO, readlines

__all__ = ["install_requires"]

filenames = ["install_requires.txt", "requires.txt", "requirements.txt"]
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
