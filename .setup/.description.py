#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["description"]
from os.path import abspath, dirname, exists, isfile, join

repo = abspath(dirname(dirname(__file__)))

description=None
filenames=["description","description.txt"]
# ./description, ./description.txt
for filename in filenames:
    file = join(repo,filename)
    if exists(file) and isfile(file):
        description = open(file).read().lstrip().rstrip()
if description is None and __name__=="__main__":
    print("SKIP: %s NOT EXISTS" % ", ".join(filenames))

if __name__=="__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k,globals()[k]))

