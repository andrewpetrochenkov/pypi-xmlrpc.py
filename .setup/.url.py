#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from __init__ import REPO, read

__all__ = ["url"]

url = None
path = os.path.join(REPO, "url.txt")
if os.path.exists(path) and os.path.isfile(path):
    url = read(path)
else:
    if __name__ == "__main__":
        print("%s NOT EXISTS" % path)
    if "URL" in os.environ:
        url = os.environ["URL"]

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
