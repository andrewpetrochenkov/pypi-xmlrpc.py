#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["entry_points"]
from os.path import *

repo = dirname(dirname(__file__))
if not repo: repo="."

# ./entry_points.txt
path = join(repo,"entry_points.txt")
if exists(path) and isfile(path):
    lines = open(path).read().splitlines()
    lines = list(filter(lambda l:l.lstrip().rstrip(),lines))
    entry_points=lines
else:
    if __name__=="__main__":
        print("SKIP: %s NOT EXISTS" % path)

if __name__=="__main__":
	for k in __all__:
		if k in globals():
			print("%s: %s" % (k,globals()[k]))
