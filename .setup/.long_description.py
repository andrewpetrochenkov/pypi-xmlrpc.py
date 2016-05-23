#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from __init__ import REPO, read

__all__ = ["long_description"]

for name in ["README.rst", "README", "README.txt"]:
    fullpath = os.path.join(REPO, name)
    if not os.path.exists(fullpath):
        continue
    if not os.path.isfile(fullpath):
        continue
    long_description = read(fullpath)
    break

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
