#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["dependency_links"]
from os.path import *

dir = dirname(dirname(__file__))
if not dir: dir="."

lines=[]
for name in ["dependency_links.txt","dependency.txt"]:
    file = join(dir,name)
    if exists(file) and isfile(file):
        lines = open(file).read().splitlines()
        lines = list(filter(lambda l:l.lstrip().rstrip(),lines))
        dependency_links+=lines
if lines:
	dependency_links = lines

if __name__=="__main__":
	for k in __all__:
		if k in globals():
			print("%s: %s" % (k,globals()[k]))

