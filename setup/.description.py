#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["description"]
from os.path import *

dir = dirname(dirname(__file__))
if not dir: dir="."

file = join(dir,"description")
if exists(file):
    description = open(file).read().lstrip().rstrip()

if __name__=="__main__":
	for k in __all__:
		if k in globals():
			print("%s: %s" % (k,globals()[k]))

