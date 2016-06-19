#!/usr/bin/env python
# -*- coding: utf-8 -*-
import imp
import os
import sys
import warnings

__all__ = ["REPO", "read", "readlines", "load_module"]

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


def isstring(value):
    try:
        int(value)
        return False
    except ValueError:
        return True
    except Exception:
        return False


def info(string):
    if len(sys.argv) == 1:
        print(string)


def main():
    sys.modules["__main__"].__all__ = []
    os.chdir(REPO)

    _setup = os.path.abspath(os.path.dirname(__file__))
    files = _pyfiles(_setup)
    # RuntimeWarning: Parent module 'modname' not found while handling
    # absolute import
    warnings.simplefilter("ignore", RuntimeWarning)

    for file in files:
        try:
            fullpath = os.path.join(_setup, file)
            module = load_module(fullpath)
            kwargs = moduledict(module)
            _update(**kwargs)
            if kwargs:
                info(".setup/%s: %s" % (file[1:], kwargs))
        except AttributeError:  # variable from __all__ not initialized
            continue
    # ~/.setup_kwargs.py
    fullpath = os.path.join(os.environ["HOME"], ".setup_kwargs.py")
    if os.path.exists(fullpath):
        module = load_module(fullpath)
        setup_kwargs = moduledict(module)

        _update(**setup_kwargs)
        info("%s: %s" % ("~/.setup_kwargs.py", setup_kwargs))
    else:
        info("SKIP: %s NOT EXISTS" % fullpath)

    kwargs = moduledict(sys.modules["__main__"])
    if "name" in kwargs:
        name = kwargs["name"]
        del kwargs["name"]

    if len(sys.argv) == 1 and kwargs:  # debug
        print('\nsetup(name="%s",' % name)
        for i, key in enumerate(sorted(list(kwargs.keys())), 1):  # python3
            value = kwargs[key]
            str_value = '"%s"' % value if isstring(value) else value
            comma = "," if i != len(kwargs) else ""
            print("    %s = %s%s" % (key, str_value, comma))
        print(')')

    # 1) distutils (Python Standart Library)
    #   https://docs.python.org/2/distutils/setupscript.html
    #   https://docs.python.org/2/distutils/apiref.html (arguments)
    # 2) setuptools (extra commands and arguments)
    #   extra commands:
    # http://pythonhosted.org/setuptools/setuptools.html#command-reference
    #   extra arguments:
    # http://pythonhosted.org/setuptools/setuptools.html#new-and-changed-setup-keywords
    setuptools = True
    if "--manifest-only" in sys.argv:  # distutils only
        setuptools = False
    if setuptools:
        try:
            import setuptools
            if "install" in sys.argv:
                print("setuptools.__version__: %s" % setuptools.__version__)
            setup = setuptools.setup
            if "zip_safe" not in kwargs:
                kwargs["zip_safe"] = False
        except ImportError:
            setuptools = False
    if not setuptools:
        if "install" in sys.argv:
            import distutils
            print("distutils.__version__: %s" % distutils.__version__)
        from distutils.core import setup

    if len(sys.argv) == 1:
        return
    setup(name=name, **kwargs)

if __name__ == "__main__":
    main()
