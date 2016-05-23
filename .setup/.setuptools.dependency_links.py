#!/usr/bin/env python
# setuptools setup(...,dependency_links=[]) keyword
import os
from __init__ import REPO, readlines

__all__ = ["dependency_links"]

dependency_links = []
filenames = ["dependency_links.txt", "dependency.txt"]
for filename in filenames:
    path = os.path.join(REPO, filename)
    dependency_links += readlines(path)

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
