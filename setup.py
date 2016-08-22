#!/usr/bin/env python
import os
try:
    from setupfiles import setup
except ImportError:
    from distutils.core import setup

kwargs = dict()

# known-issues:
# pip attempts to discover all of the dependencies before installation
# python setup.py egg_info
install_requires = []
path = os.path.join(os.getcwd(), "requirements.txt")
if os.path.exists(path) and os.path.isfile(path):
    kwargs["install_requires"] = open(path).read().splitlines()

setup(**kwargs)
