#!/usr/bin/env python
import pypi_xmlrpc

packages = pypi_xmlrpc.list_packages()
print("%s packages" % len(packages))
