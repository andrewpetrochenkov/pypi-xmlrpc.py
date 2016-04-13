#!/usr/bin/env python
# setuptools setup(...,install_requires=[]) keyword
# checks that the requirements installed
# raise exception if requirements not installed:
# error: Could not find required distribution <name>
# fix - install requirements.txt first:
# 1) pip install -U <name>
# 2) pip install -r requirements.txt; python install setup.py
__all__=["install_requires"]
from os.path import abspath, dirname, exists, join

repo = abspath(dirname(dirname(__file__)))

install_requires = []
for name in ["requirements.txt","requires.txt","install_requires.txt"]:
    file = join(repo,name)
    if exists(file):
        lines = open(file).read().splitlines()
        lines = list(filter(lambda l:l.lstrip().rstrip(),lines))
        install_requires=lines

if __name__=="__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k,globals()[k]))
