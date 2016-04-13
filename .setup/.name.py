#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__ = ["name"]
from os.path import abspath, basename, dirname

repo = abspath(dirname(dirname(__file__)))

# default pkgname
name = basename(repo).lower().split(".")[0]


if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
