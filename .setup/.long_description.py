#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["long_description"]
from os.path import abspath, dirname, exists, isfile, join


repo = abspath(dirname(dirname(__file__)))

for name in ["README.rst","README","README.txt"]:
    fullpath = join(repo,name)
    if not exists(fullpath): continue
    if not isfile(fullpath): continue
    long_description = open(fullpath).read()

if __name__=="__main__":
	for k in __all__:
		if k in globals():
			print("%s: %s" % (k,globals()[k]))

