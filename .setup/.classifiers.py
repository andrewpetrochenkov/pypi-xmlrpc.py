#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from __init__ import HOME, REPO, readlines

__all__ = ["classifiers"]

classifiers = []
# ~/.classifiers.txt (default)
# ./.classifiers.txt, ./classifiers.txt (custom)
for path in [
        os.path.join(HOME, ".classifiers.txt"),
        os.path.join(REPO, ".classifiers.txt"),
        os.path.join(REPO, "classifiers.txt")]:
    if os.path.exists(path) and os.path.isfile(path):
        for l in readlines(path):
            if l and " :: " in l and "#" not in l:
                classifiers.append(l)
classifiers = sorted(list(set(classifiers)))

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
