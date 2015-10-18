#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["install_requires"]
import os
from os.path import *


dir = dirname(dirname(__file__))
if not dir: dir="."

install_requires = []
# skip if ~/.no_install_requires exists
no_install_requires = join(os.environ["HOME"],".no_install_requires")
if exists(no_install_requires):
	for name in ["requirements.txt","requires.txt","install_requires.txt"]:
	    file = join(dir,name)
	    if exists(file):
	        lines = open(file).read().splitlines()
	        lines = list(filter(lambda l:l.lstrip().rstrip(),lines))
	        install_requires=lines

	if __name__=="__main__":
	    for k in __all__:
	        if k in globals():
	            print("%s: %s" % (k,globals()[k]))
else:
	print("%s: SKIP ~/.no_install_requires" % __file__)

