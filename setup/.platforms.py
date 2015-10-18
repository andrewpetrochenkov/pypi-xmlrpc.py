#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["platforms"]
from os.path import *

dir = dirname(dirname(__file__))
if not dir: dir="."

file = join(dir,"platforms.txt")
platforms="any" # default
if exists(file):
    platforms = open(file).read().lstrip().rstrip()

if __name__=="__main__":
	for k in __all__:
		if k in globals():
			print("%s: %s" % (k,globals()[k]))

