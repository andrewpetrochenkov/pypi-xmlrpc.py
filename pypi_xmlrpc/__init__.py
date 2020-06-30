__all__ = ['list_packages', 'user_packages',
           'release_urls', 'package_roles', 'package_releases', 'release_data']


try:
    from xmlrpclib import ServerProxy
except ImportError:
    from xmlrpc.client import ServerProxy

pypi = ServerProxy('https://pypi.org/pypi', allow_none=True)


def list_packages():
    """return a list of all server packages"""
    return pypi.list_packages()


def user_packages(user):
    """return a list of user packages"""
    return pypi.user_packages(user)


def release_urls(name, version):
    """return a list of release urls"""
    return pypi.release_urls(name, version)


def package_roles(name):
    """return a list of package roles"""
    return pypi.package_roles(name)


def package_releases(name, show_hidden=True):
    """return a list of package releases"""
    return pypi.package_releases(name, show_hidden)


def release_data(name, version):
    """return dictionary with release data"""
    return pypi.release_data(name, version)
