#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from __init__ import REPO, load_module

__all__ = ["data_files"]

data_files = []
path = os.path.join(REPO, "data_files.py")
if os.path.exists(path):
    module = load_module(path)
    if hasattr(module, "data_files"):
        data_files = module.data_files
else:
    if __name__ == "__main__":
        print("SKIP: %s NOT EXISTS" % path)

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
