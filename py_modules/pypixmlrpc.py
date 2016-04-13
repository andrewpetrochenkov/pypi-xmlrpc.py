#!/usr/bin/env python
from datetime import *
try:
    from xmlrpclib import *  # python2
except ImportError:
    from xmlrpc.client import *  # python3
# 3DP
import requests
# me
from dict import *
from public import public


@public
class Server:
    url = None

    def __init__(self, url='http://pypi.python.org/pypi'):
        self.url = url

    @property
    def _ServerProxy(self):
        return ServerProxy(self.url, allow_none=True)

    def json(self, package, version=None):
        """return json"""
        if version:
            url = "http://pypi.python.org/pypi/%s/%s/json" % (package, version)
        else:
            url = "http://pypi.python.org/pypi/%s/json" % package
        r = requests.get(url)
        if r.status_code == 200:
            return dict(r.json)
        else:
            r.raise_for_status()

    def list_packages(self):
        """
        Retrieve a list of the package names registered with the package index. Returns a list of name strings
        """
        packages = self._ServerProxy.list_packages()
        return packages

    def package_releases(self, name, show_hidden=True):
        """
        Retrieve a list of the releases registered for the given package_name. Returns a list with all version strings if show_hidden is True or only the non-hidden ones otherwise
        """
        releases = self._ServerProxy.package_releases(name, show_hidden)
        return releases

    def package_roles(self, package_name):
        """
        Retrieve a list of users and their attributes roles for a given package_name. Role is either 'Maintainer' or 'Owner'
        """
        return self._ServerProxy.package_roles(package_name)

    def release_data(self, name, version):
        """
        Retrieve metadata describing a specific package release. Returns a dict with keys for
        """
        data = dict(
            self._ServerProxy.release_data(name, version)
        )
        for k in data.keys():
            if data[k] == 'UNKNOWN':
                data[k] is None
        return data

    def release_downloads(self, package_name, version):
        """
        Retrieve a list of files and download count for a given package and release version
        """
        return dict(
            self._ServerProxy.release_downloads(package_name, version)
        )

    def release_urls(self, pkg, version):
        """
        Retrieve a list of download URLs for the given package release. Returns a list of dicts with the following key
        """
        response = self._ServerProxy.release_urls(pkg, version)
        list = []
        for d in response:
            dt = datetime.strptime(str(d["upload_time"]))
            d["upload_time"] = dt.isoformat()
            list.append(d)
        return dict(list)

    def user_packages(self, user):
        """
        Retrieve a list of [role_name, package_name] for a given username. Role is either 'Maintainer' or 'Owner'
        """
        return self._ServerProxy.user_packages(user)


pypi = Server('http://pypi.python.org/pypi')
public(pypi)

if __name__ == "__main__":
    import os
    from os.path import *
    offline = join(os.environ["HOME"], ".offline")
    if not exists(offline):
        print(pypi.list_packages())
        print(pypi.user_packages("kennethreitz"))  # user_packages
        print(pypi.package_roles("requests"))
