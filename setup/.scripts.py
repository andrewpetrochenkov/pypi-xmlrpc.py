#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["scripts"]
import os
from os.path import *

dir = dirname(dirname(__file__))
if not dir: dir="."

file = join(dir,"scripts.txt")
if exists(file) and isfile(file): # ./url.txt
    scripts = open(file).read().lstrip().rstrip().splitlines()
else:
    path  = join(dir,"scripts")
    if exists(path) and isdir(file):
        scripts = list(map(lambda name:join("scripts",name),
            list(filter(lambda f:isfile(join(path,f)) and f.find(" ")<0,
                os.listdir(path)
            ))
        ))

if __name__=="__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k,globals()[k]))
