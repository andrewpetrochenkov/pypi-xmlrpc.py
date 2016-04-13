#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["data_files"]
import imp
from os.path import *

repo = abspath(dirname(dirname(__file__)))

def load_module(path):
    with open(path,'rb') as fp:
        # .hidden.py invisible for mdfind
        module = imp.load_module(path,fp,path,('.py', 'rb', imp.PY_SOURCE))
        # __all__ required
        if not hasattr(module,'__all__'):
            raise ValueError("ERROR: %s __all__ required" % path)
        return module

data_files = []
path=join(repo,"data_files.py")
if exists(path):
	module = load_module(path)
	if hasattr(module,"data_files"):
		data_files = module.data_files
else:
    if __name__=="__main__":
        print("SKIP: %s NOT EXISTS" % path)

if __name__=="__main__":
	for k in __all__:
		if k in globals():
			print("%s: %s" % (k,globals()[k]))

