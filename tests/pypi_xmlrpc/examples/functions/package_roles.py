#!/usr/bin/env python
import pypi_xmlrpc

name = "requests"
package_roles = pypi_xmlrpc.package_roles(name)
for role, name in package_roles:
    print("%s (%s)" % (name, role))
