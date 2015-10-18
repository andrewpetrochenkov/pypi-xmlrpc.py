#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["version"]
from os.path import *

dir = dirname(dirname(__file__))
if not dir: dir="."

# ./version or ./version.txt
for name in ["version","version.txt"]:
    file = join(dir,name)
    if exists(file) and isfile(file):
        version = open(file).read().lstrip().rstrip()

if __name__=="__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k,globals()[k]))
