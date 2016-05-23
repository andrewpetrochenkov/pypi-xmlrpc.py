#!/usr/bin/env python
# -*- coding: utf-8 -*-
import imp
import os
import sys
import warnings

__all__ = ["REPO", "read", "readlines", "load_module"]

# __pycache__/ conflict with setuptools
sys.dont_write_bytecode = True  # REQUIRED!

# 1) distutils (Python Standart Library)
#   docs.python.org/2/distutils/setupscript.html
#   docs.python.org/3/distutils/setupscript.html
# python setup.py --manifest-only
# 2) setuptools (+easy_install tool)
#   pypi.python.org/pypi/setuptools
#   pythonhosted.org/setuptools/setuptools.html

# setuptools additional setup(name,**kwargs) keywords
SETUPTOOLS_KWARGS = [
    "include_package_data",  # True/False
    "exclude_package_data",  # True/False
    "package_data",  # True/False
    "zip_safe",  # True/False
    "install_requires",  # [...]
    "entry_points",  # [...]
    "extras_require",  # [...]
    "setup_requires",  # [...]
    "dependency_links",  # [...]
    "namespace_packages",  # [...]
    "test_suite",  # ''
    "tests_require",  # ''
    "test_loader"  # ''
]
# setuptools `python setup.py` Extra commands (python setup.py --help):
SETUPTOOLS_ARGS = [
    # save supplied options to setup.cfg or other config file
    "saveopts",
    # Run unit tests using testr
    "testr",
    # install package in 'development mode'
    "develop",
    # Upload documentation to PyPI
    "upload_docs",
    # run unit tests after in-place build
    "test",
    # set an option in setup.cfg or another config file
    "setopt",
    # Run unit tests using nosetests
    "nosetests",
    # Install an .egg-info directory for the package
    "install_egg_info",
    # delete older distributions, keeping N newest files
    "rotate",
    # create a Mac OS X mpkg distribution for Installer.app
    "bdist_mpkg",
    # create a distribution's .egg-info directory
    "egg_info",
    # create a Mac OS X application or plugin from Python scripts
    "py2app",
    # define a shortcut to invoke one or more commands
    "alias",
    # Find/get/install Python packages
    "easy_install",
    # create an "egg" distribution
    "bdist_egg"
]

REPO = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def read(path):
    if os.path.exists(path) and os.path.isfile(path):
        value = open(path).read().lstrip().rstrip()
        if value:
            return value


def readlines(path):
    if os.path.exists(path) and os.path.isfile(path):
        lines = open(path).read().splitlines()
        lines = list(filter(lambda l: l.lstrip().rstrip(), lines))
        lines = list(filter(lambda l: l, lines))
        return lines
    return []


def _pyfiles(path):
    """find python files of a directory"""
    listdir = os.listdir(path)
    listdir = filter(lambda l: os.path.splitext(
        l)[1] == ".py" and l.find("__") < 0, listdir)
    return listdir


def moduledict(module):
    """get module public objects dict"""
    kwargs = dict()
    for k in getattr(module, "__all__"):
        if getattr(module, k):
            kwargs[k] = getattr(module, k)
    return kwargs


def load_module(path):
    with open(path, 'rb') as fhandler:
        # .hidden.py invisible for mdfind
        module = imp.load_module(
            path, fhandler, path, ('.py', 'rb', imp.PY_SOURCE))
        # __all__ required
        if not hasattr(module, '__all__'):
            raise ValueError("ERROR: %s __all__ required" % path)
        return module


def _update(**kwargs):
    for key, value in kwargs.items():
        if key not in sys.modules["__main__"].__all__:
            sys.modules["__main__"].__all__.append(key)
        setattr(sys.modules["__main__"], key, value)


def _isstring(value):
    try:
        int(value)
        return False
    except ValueError:
        return True
    except Exception:
        return False


def main():
    sys.modules["__main__"].__all__ = []
    os.chdir(REPO)

    files = _pyfiles(os.path.dirname(__file__))
    # RuntimeWarning: Parent module 'modname' not found while handling
    # absolute import
    warnings.simplefilter("ignore", RuntimeWarning)

    for file in files:
        try:
            fullpath = os.path.join(os.path.dirname(__file__), file)
            module = load_module(fullpath)
            kwargs = moduledict(module)
            _update(**kwargs)
            if len(sys.argv) == 1 and len(kwargs) > 0:
                print("%s: %s" % (file[1:], kwargs))
        except AttributeError:  # variable from __all__ not initialized
            continue
    # ~/.setup_kwargs.py
    fullpath = os.path.join(os.environ["HOME"], ".setup_kwargs.py")
    if os.path.exists(fullpath):
        module = load_module(fullpath)
        setup_kwargs = moduledict(module)

        _update(**setup_kwargs)
        if len(sys.argv) == 1 and len(setup_kwargs) > 0:  # debug
            print("%s: %s" % ("~/.setup_kwargs.py", setup_kwargs))

    kwargs = moduledict(sys.modules["__main__"])
    if "name" in kwargs:
        name = kwargs["name"]
        del kwargs["name"]

    if len(sys.argv) == 1 and kwargs:  # debug
        print('\nsetup(name="%s",' % name)
        # for i,(k,v) in enumerate(sorted(kwargs.iteritems(),key=lambda
        # (k,v):k),1): # python2
        for i, key in enumerate(sorted(list(kwargs.keys())), 1):  # python3
            value = kwargs[key]
            str_value = '"%s"' % value if _isstring(value) else value
            comma = "," if i != len(kwargs) else ""
            print("    %s = %s%s" % (key, str_value, comma))
        print(')')

    setuptools = False  # check for setuptools
    # `python setup.py` args
    for arg in SETUPTOOLS_ARGS:
        if arg in sys.argv:
            setuptools = True
    # setup(name,**kwargs) kwargs
    for arg in SETUPTOOLS_KWARGS:
        if arg in kwargs and kwargs[arg] is not None:
            value = kwargs[arg]
            if value != [] and value != "" and value != {} and value:
                # sys.stderr.write("setuptools arg = %s" % arg)
                setuptools = True

    if sys.argv[-1] == "--manifest-only":  # distutils only
        setuptools = False

    if setuptools:
        try:
            if sys.argv[-1] == "install":
                print("from setuptools import setup")
            from setuptools import setup
            kwargs["zip_safe"]=False
        except ImportError:
            if sys.argv[-1] == "install":
                print("setuptools not installed")  # use distutils
            if sys.argv[-1] == "install":
                print("from distutils.core import setup")
            from distutils.core import setup  # default
    else:
        if sys.argv[-1] == "install":
            print("from distutils.core import setup")
        from distutils.core import setup  # default

    if len(sys.argv) == 1:
        return
    setup(name=name, **kwargs)

if __name__ == "__main__":
    main()
