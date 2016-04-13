#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__ = ["py_modules", "package_dir"]
import os
from os.path import abspath, dirname, exists, isdir, isfile, join, splitext

repo = abspath(dirname(dirname(__file__)))

path = join(repo, "py_modules")
if exists(path) and isdir(path):  # ./py_modules/
    listdir = os.listdir(path)
    pyfiles = list(filter(lambda l: splitext(l)[1] == ".py", listdir))
    pyfiles = list(filter(lambda f: isfile(join(path, f)), pyfiles))
    py_modules = list(map(lambda f: f.replace(".py", ""), pyfiles))
    if py_modules:
        package_dir = {'': "py_modules"}
else:
    if __name__ == "__main__":
        print("SKIP: %s/ NOT EXISTS" % path)

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
