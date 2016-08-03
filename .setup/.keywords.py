#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from __init__ import REPO, read

__all__ = ["keywords"]

path = os.path.join(REPO, "keywords.txt")  # separated by " " space
if os.path.exists(path) and os.path.isfile(path):
    keywords = read(path)
else:
    if __name__ == "__main__":
        print("SKIP: %s NOT EXISTS" % path)
    if "KEYWORDS" in os.environ:
        keywords = os.environ["KEYWORDS"]

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
