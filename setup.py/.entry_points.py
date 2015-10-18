#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["entry_points"]
from os.path import *

dir = dirname(dirname(__file__))
if not dir: dir="."

# ./entry_points.txt
file = join(dir,"entry_points.txt")
if exists(file) and isfile(file):
    lines = open(file).read().splitlines()
    lines = list(filter(lambda l:l.lstrip().rstrip(),lines))
    entry_points=lines

if __name__=="__main__":
	for k in __all__:
		if k in globals():
			print("%s: %s" % (k,globals()[k]))
