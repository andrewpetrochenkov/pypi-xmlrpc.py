#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from __init__ import REPO

__all__ = ["name"]

# default pkgname
name = os.path.basename(REPO).split(".")[0]
if "NAME" in os.environ:
    name = os.environ["NAME"]

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
