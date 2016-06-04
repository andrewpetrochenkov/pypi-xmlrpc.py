#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from __init__ import REPO

__all__ = ["packages", "package_dir", "package_data"]

# distname.py/
# distname.py/packages/
# distname.py/packages/pkgname1/
# distname.py/packages/pkgname2/


def _packages(path):
    listdir = os.listdir(path)
    for l in listdir:
        if os.path.exists(os.path.join(path, l, "__init__.py")):
            yield l

path = os.path.join(REPO, "packages")
if os.path.exists(path) and os.path.isdir(path):
    packages = list(_packages(path))
    if packages:
        package_dir = dict()
        package_data = dict()
        for package in packages:
            package_dir[package] = "packages/%s" % package
            package_data[package] = ['*']
else:
    if __name__ == "__main__":
        print("SKIP: %s/ NOT EXISTS" % path)

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
