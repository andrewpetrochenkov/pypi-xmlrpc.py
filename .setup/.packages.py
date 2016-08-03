#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from __init__ import REPO

__all__ = ["packages", "package_dir", "package_data"]

# repo/
# repo/packages/
# repo/packages/pkgname1/*.py
# repo/packages/pkgname1/data/*
# repo/packages/pkgname2/*.py
# repo/packages/pkgname2/data/*


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
            path = "packages/%s" % package
            package_dir[package] = path
            data = '%s/data' % path
            if os.path.exists(data):
                package_data[package] = ['data/*']
else:
    if __name__ == "__main__":
        print("%s/ NOT EXISTS" % path)

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
