<!--
README generated with readmemako.py (github.com/russianidiot/readme-mako.py) and .README dotfiles (github.com/russianidiot-dotfiles/.README)
-->

![python](https://img.shields.io/badge/language-python-blue.svg)
[![PyPI](https://img.shields.io/pypi/pyversions/pypixmlrpc.svg)](https://pypi.python.org/pypi/pypixmlrpc)[![PyPI](https://img.shields.io/pypi/v/pypixmlrpc.svg)](https://pypi.python.org/pypi/pypixmlrpc)

[![codacy.com](https://api.codacy.com/project/badge/Grade/2d0aefd518834ab49eb01c0d475fcef9)](https://www.codacy.com/app/russianidiot-github/pypixmlrpc-py/dashboard)
[![landscape.io](https://landscape.io/github/russianidiot/pypixmlrpc.py/master/landscape.svg?style=flat)](https://landscape.io/github/russianidiot/pypixmlrpc.py)
[![codeclimate.com](https://codeclimate.com/github/russianidiot/pypixmlrpc.py/badges/gpa.svg)](https://codeclimate.com/github/russianidiot/pypixmlrpc.py)
[![scrutinizer-ci.com](https://scrutinizer-ci.com/g/russianidiot/pypixmlrpc.py/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/russianidiot/pypixmlrpc.py/)

[![drone.io](https://drone.io/github.com/russianidiot/pypixmlrpc.py/status.png)](https://drone.io/github.com/russianidiot/pypixmlrpc.py)
[![scrutinizer-ci.com](https://scrutinizer-ci.com/g/russianidiot/pypixmlrpc.py/badges/build.png?b=master)](https://scrutinizer-ci.com/g/russianidiot/pypixmlrpc.py/)
[![semaphoreci.com](https://semaphoreci.com/api/v1/russianidiot/pypixmlrpc-py/branches/master/shields_badge.svg)](https://semaphoreci.com/russianidiot/pypixmlrpc-py)
[![shippable.com](https://api.shippable.com/projects/57068cbb2a8192902e1bbbd8/badge?branch=master)](https://app.shippable.com/projects/57068cbb2a8192902e1bbbd8/status/)
[![travis-ci.org](https://api.travis-ci.org/russianidiot/pypixmlrpc.py.svg)](https://travis-ci.org/russianidiot/pypixmlrpc.py)
[![wercker.com](https://app.wercker.com/status/dcbb3555061ed95f4da533e02bbc4d98/s/master)](https://app.wercker.com/#applications/5702b5e6a7bb73af2515f8d7)

<p align="center">
    <b>pypi XML-RPC wrapper</b>
</p>

#### Install

`[sudo] pip install pypixmlrpc`

```python
>>> from pypixmlrpc import *

>>> pypi.list_packages()

>>> pypi.user_packages("kennethreitz") # user packages

>>> pypi.package_releases("requests")

>>> pypi.package_roles("requests")

>>> version="x.y.z"
>>> pypi.release_data("requests",version)
>>> pypi.release_downloads("requests",version)
>>> pypi.release_urls("requests",version)
```

[Examples/](https://github.com/russianidiot/pypixmlrpc.py/tree/master/Examples)

### Links
*	PyPiXmlRpc - PythonInfo Wiki - [wiki.python.org/moin/PyPiXmlRpc](http://wiki.python.org/moin/PyPiXmlRpc)

Feedback
[![GitHub issues](https://img.shields.io/github/issues/russianidiot/pypixmlrpc.py.svg)](https://github.com/russianidiot/pypixmlrpc.py/issues)
[![Join the chat at https://gitter.im/russianidiot/pypixmlrpc.py](https://badges.gitter.im/russianidiot/pypixmlrpc.py.svg)](https://gitter.im/russianidiot/pypixmlrpc.py)
[![GitHub followers](https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow)](https://github.com/russianidiot)
