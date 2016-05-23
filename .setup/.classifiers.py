#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from __init__ import readlines

__all__ = ["classifiers"]

HOME = os.environ["HOME"]

classifiers = []
# ~/.classifiers.txt (default)
default = readlines(os.path.join(HOME, ".classifiers.txt"))
# ./.classifiers.txt, ./classifiers.txt (custom, override default)
custom = readlines(".classifiers.txt") + readlines("classifiers.txt")
for l in custom:
    if l.find(" :: ") > 0:
        k = l.split(" :: ")[0]
        default = list(filter(lambda l: l.find(k) != 0, default))
classifiers = sorted(default + custom)

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
