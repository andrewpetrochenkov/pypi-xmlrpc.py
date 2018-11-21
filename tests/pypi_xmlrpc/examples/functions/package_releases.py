#!/usr/bin/env python
import pypi_xmlrpc

package_name = "requests"
package_releases = pypi_xmlrpc.package_releases(package_name)
print(package_releases)
