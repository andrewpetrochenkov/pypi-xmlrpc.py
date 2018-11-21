#!/usr/bin/env python
import pypi_xmlrpc

name = "requests"

package_releases = pypi_xmlrpc.package_releases(name)
version = package_releases[0]

data = pypi_xmlrpc.release_data(name, version)
print(data)
