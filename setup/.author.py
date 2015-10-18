#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["author"]
try:
	from ConfigParser import * # python2
except:
	from configparser import * # python3
from os.path import *

# username
# https://docs.python.org/2/distutils/packageindex.html#pypirc
path = expanduser("~/.pypirc")
if exists(path):
    cfg = RawConfigParser()
    cfg.read(path)
    if cfg.has_option("pypi","username"):
        author = cfg.get('pypi', 'username')

if __name__=="__main__":
	for k in __all__:
		if k in globals():
			print("%s: %s" % (k,globals()[k]))

