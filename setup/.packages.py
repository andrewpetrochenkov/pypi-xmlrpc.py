#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["packages"]
import os
from os.path import *

dir = dirname(dirname(__file__))
if not dir: dir="."


file = join(dir,"packages.txt")
if exists(file):
    packages = open(file).read().lstrip().rstrip().splitlines()
else:
    # packages
    names = os.listdir(dir)
    names = list(filter(lambda _:_.lower()!="tests",names)) # exclude "tests"
    names = list(filter(lambda _:_.lower()!="setup",names)) # exclude "setup"
    names = list(filter(lambda name:name.find(".")<0,names)) # exclude *.* names with dot
    fullpaths = list(map(lambda name:join(dir,name),names))
    dirs = list(filter(lambda path:isdir(path),fullpaths))
    packages = list(filter(lambda path:exists(join(path,"__init__.py")),dirs))
    packages = list(map(basename,packages))

if __name__=="__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k,globals()[k]))
