#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__ = ["scripts"]
import os
from os.path import *

def valid_script_name(name):
    return name[0] != "." and " " not in name


repo = abspath(dirname(dirname(__file__)))

path = join(repo, "scripts")
if exists(path) and isdir(path):
    listdir = filter(valid_script_name, os.listdir(path))
    find = map(lambda name: join(path, name), listdir)
    files = filter(isfile, find)
    scripts = list(map(lambda name: "scripts/%s" % basename(name), files))
    for script in scripts:
        dst = join("/usr/local/bin/%s" % basename(script))
        if exists(dst) and not isfile(dst):
            print("ERROR: %s EXISTS and NOT FILE" % dst)
else:
    if __name__ == "__main__":
        print("SKIP: %s/ NOT EXISTS" % path)

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))
