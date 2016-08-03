#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from __init__ import REPO

__all__ = ["py_modules", "package_dir"]


def _py_modules(path):
    listdir = os.listdir(path)
    for l in listdir:
        if os.path.splitext(l)[1] != ".py":
            continue
        fullpath = os.path.join(path, l)
        if not os.path.isfile(fullpath):
            continue
        yield l.replace(".py", "")

path = os.path.join(REPO, "py_modules")
if os.path.exists(path) and os.path.isdir(path):  # ./py_modules/
    py_modules = list(_py_modules(path))
    if py_modules:
        package_dir = {'': "py_modules"}
else:
    if __name__ == "__main__":
        print("%s/ NOT EXISTS" % path)

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
