#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__=["bugtrack_url"]
import os
from os.path import *
from subprocess import *

dir = dirname(dirname(__file__))
if not dir: dir="."

file = join(dir,"bugtrack_url.txt")
if exists(file) and isfile(file):
    bugtrack_url = open(file).read().lstrip().rstrip()
else:
    if exists(join(dir,".git")): # .git repo
        args = ["git","config","user.name"]
        process = Popen(args,stdout=PIPE)
        stdout,stderr = process.communicate()
        username = stdout.rstrip()

        name = basename(dir)
        bugtrack_url="https://github.com/%s/%s/issues" % (username,name)

if __name__=="__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k,globals()[k]))

