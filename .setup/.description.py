#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from __init__ import REPO, read

__all__ = ["description"]

description = None
filenames = ["description", "description.txt"]
# ./description, ./description.txt
for filename in filenames:
    path = os.path.join(REPO, filename)
    if os.path.exists(path) and os.path.isfile(path):
        description = read(path)
if description is None and __name__ == "__main__":
    print("SKIP: %s NOT EXISTS" % ", ".join(filenames))
if not description and "DESCRIPTION" in os.environ:
    description = os.environ["DESCRIPTION"]

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
