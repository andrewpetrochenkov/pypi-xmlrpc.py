#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["classifiers"]
import os
from os.path import abspath, dirname, exists, isfile, join

HOME=os.environ["HOME"]
repo = abspath(dirname(dirname(__file__)))

def read(path):
    if exists(path) and isfile(path):
        lines = open(path).read().splitlines()
        lines = list(filter(lambda l:l.lstrip().rstrip(),lines))
        lines = list(filter(lambda l:l,lines))
        return lines
    return []

classifiers = []
# ~/.classifiers.txt (default)
default = read(join(HOME,".classifiers.txt"))
# ./.classifiers.txt, ./classifiers.txt (custom, override default)
custom=read(".classifiers.txt")+read("classifiers.txt")
for l in custom:
    if l.find(" :: ")>0:
        k = l.split(" :: ")[0]
        default = list(filter(lambda l:l.find(k)!=0,default))
classifiers=default+custom
classifiers.sort()

if __name__=="__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k,globals()[k]))
