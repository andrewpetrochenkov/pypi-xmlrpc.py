#!/usr/bin/env python
# setuptools setup(...,dependency_links=[]) keyword
__all__=["dependency_links"]
from os.path import abspath, dirname, exists, join

repo = abspath(dirname(dirname(__file__)))

lines=[]
filenames=["dependency_links.txt","dependency.txt"]
for filename in filenames:
    file = join(repo,filename)
    if exists(file) and isfile(file):
        lines = open(file).read().splitlines()
        lines = list(filter(lambda l:l.lstrip().rstrip(),lines))
        dependency_links+=lines
if lines:
	dependency_links = lines

if __name__=="__main__":
	for k in __all__:
		if k in globals():
			print("%s: %s" % (k,globals()[k]))

