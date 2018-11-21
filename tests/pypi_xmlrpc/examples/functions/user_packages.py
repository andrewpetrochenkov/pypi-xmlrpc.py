#!/usr/bin/env python
import pypi_xmlrpc

user = "kennethreitz"
packages = pypi_xmlrpc.user_packages(user)

print("%s packages (%s):" % (user, len(packages)))
for i, (role, name) in enumerate(packages, 1):
    print("%s/%s: %s (%s)" % (i, len(packages), name, role))
