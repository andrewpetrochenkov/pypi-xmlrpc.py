#!/usr/bin/env python
import os
try:
    from setupfiles import setup
except ImportError:
    from distutils.core import setup

kwargs = dict()

# known-issues:
# pip running `python setup.py egg_info` before installation:
# 1) pip checks metadata name pip/req/req_install.py:run_egg_info()
# 2) pip attempts to discover all of the dependencies before installation
name = os.path.basename(os.getcwd()).split(".")[0].lower()

path = os.path.join(os.getcwd(), "requirements.txt")
if os.path.exists(path) and os.path.isfile(path):
    kwargs["install_requires"] = open(path).read().splitlines()

setup(name=name,**kwargs)
