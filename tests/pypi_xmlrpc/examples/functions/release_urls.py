#!/usr/bin/env python
import pypi_xmlrpc

package_name = "requests"
package_releases = pypi_xmlrpc.package_releases(package_name)
version = package_releases[0]

print(version)
urls = pypi_xmlrpc.release_urls(package_name, version)
for url in urls:
    print(url)
