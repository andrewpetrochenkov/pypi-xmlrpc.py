#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["packages"]
import os
from os.path import *

repo = abspath(dirname(dirname(__file__)))

# distname.py/
# distname.py/packages/
# distname.py/packages/pkgname1/
# distname.py/packages/pkgname2/
path = join(repo,"packages")
if exists(path) and isdir(path):
    names = os.listdir(path)
    find = list(map(lambda name:join(path,name),names))
    find = list(filter(lambda path:isdir(path),find))
    find = list(filter(lambda path:exists(join(path,"__init__.py")),find))
    packages = list(map(basename,find))
else:
    if __name__=="__main__":
        print("SKIP: %s/ NOT EXISTS" % path)

if __name__=="__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k,globals()[k]))
