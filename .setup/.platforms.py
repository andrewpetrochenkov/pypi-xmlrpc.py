#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from __init__ import REPO, read

__all__ = ["platforms"]

path = os.path.join(REPO, "platforms.txt")
if os.path.exists(path) and os.path.isfile(path):
    platforms = read(path)
else:
    if __name__ == "__main__":
        print("SKIP: %s NOT EXISTS" % path)

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
