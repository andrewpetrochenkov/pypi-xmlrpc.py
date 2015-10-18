#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["keywords"]
from os.path import *

dir = dirname(dirname(__file__))
if not dir: dir="."

file = join(dir,"keywords.txt")
if exists(file):
	# separated by " " space
    keywords = open(file).read().lstrip().rstrip()

if __name__=="__main__":
	for k in __all__:
		if k in globals():
			print("%s: %s" % (k,globals()[k]))

