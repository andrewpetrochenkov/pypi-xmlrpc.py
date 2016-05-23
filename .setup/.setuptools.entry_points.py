#!/usr/bin/env python
# setuptools setup(...,entry_points=[]) keyword
import os
from __init__ import REPO, readlines

__all__ = ["entry_points"]

# ./entry_points.txt
path = os.path.join(REPO, "entry_points.txt")
if os.path.exists(path) and os.path.isfile(path):
    entry_points = readlines(path)
else:
    if __name__ == "__main__":
        print("SKIP: %s NOT EXISTS" % path)

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
