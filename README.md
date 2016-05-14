![python](https://img.shields.io/badge/language-python-blue.svg)[![PyPI](https://img.shields.io/pypi/pyversions/pypixmlrpc.svg)](https://pypi.python.org/pypi/pypixmlrpc)

[![codacy.com](https://img.shields.io/codacy/2d0aefd518834ab49eb01c0d475fcef9.svg)](https://www.codacy.com/app/russianidiot-github/pypixmlrpc-py/dashboard)[![landscape.io](https://landscape.io/github/russianidiot/pypixmlrpc.py/master/landscape.svg?style=flat)](https://landscape.io/github/russianidiot/pypixmlrpc.py/master)[![Code Climate](https://img.shields.io/codeclimate/github/russianidiot/pypixmlrpc.py.svg)](https://codeclimate.com/github/russianidiot/pypixmlrpc.py)
[![Code Health](https://scrutinizer-ci.com/g/russianidiot/pypixmlrpc.py/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/russianidiot/pypixmlrpc.py)

[![Build Status](https://travis-ci.org/russianidiot/pypixmlrpc.py.svg?branch=master)](https://travis-ci.org/russianidiot/pypixmlrpc.py)[![drone.io](https://drone.io/github.com/russianidiot/pypixmlrpc.py/status.png)](https://drone.io/github.com/russianidiot/pypixmlrpc.py)[![Wercker](https://img.shields.io/wercker/ci/russianidiot/pypixmlrpc.py.svg)](https://app.wercker.com/#applications/5702b5e6a7bb73af2515f8d7/)
[![codecov.io](https://codecov.io/github/russianidiot/pypixmlrpc.py/coverage.svg?branch=master)](https://codecov.io/github/russianidiot/pypixmlrpc.py?branch=master)

[![PyPI](https://img.shields.io/pypi/v/pypixmlrpc.svg)](https://pypi.python.org/pypi/pypixmlrpc)
[![PyPI](https://img.shields.io/pypi/dm/pypixmlrpc.svg)](https://pypi.python.org/pypi/pypixmlrpc)
[![PyPI](https://img.shields.io/pypi/dd/pypixmlrpc.svg)](https://pypi.python.org/pypi/pypixmlrpc)

<p align="center">
    <b>pypi XML-RPC wrapper</b>
</p>

#### Install

pip: 
`[sudo] pip install pypixmlrpc`

#### Usage
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

Sources:
*	[py_modules/pypixmlrpc.py](https://github.com/russianidiot/pypixmlrpc.py/blob/master/py_modules/pypixmlrpc.py)

### Links

*	PyPiXmlRpc - PythonInfo Wiki - [wiki.python.org/moin/PyPiXmlRpc](http://wiki.python.org/moin/PyPiXmlRpc)

Feedback
[![GitHub issues](https://img.shields.io/github/issues/russianidiot/pypixmlrpc.py.svg)](https://github.com/russianidiot/pypixmlrpc.py/issues)
[![Join the chat at https://gitter.im/russianidiot/pypixmlrpc.py](https://badges.gitter.im/russianidiot/pypixmlrpc.py.svg)](https://gitter.im/russianidiot/pypixmlrpc.py)
[![GitHub followers](https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow)](https://github.com/russianidiot)

* * *

<p align="center">
	Python packages <a href="http://russianidiot.github.io/python/">russianidiot.github.io/python/</a>
	<img src="http://russianidiot.github.io/images/python/16.png" />
</p>
<p align="center">
	cli packages <a href="http://russianidiot.github.io/python/">russianidiot.github.io/cli/</a>
<img src="http://russianidiot.github.io/images/cli/16.png" />
</p>

<p align="center">
	repos list <a href="http://russianidiot.github.io/">russianidiot.github.io</a> <img src="http://russianidiot.github.io/images/star/16.png" />
</p>

<p align="center">
	<a href="https://raw.githubusercontent.com/russianidiot/pypixmlrpc.py/master/README.md">README.md</a> generated with <a href="https://github.com/russianidiot/readme-mako.py">readmemako.py</a> (python+<a href="http://www.makotemplates.org/">mako</a> templates) and <a href="https://github.com/russianidiot-dotfiles/.README">.README</a> dotfiles 
<img src="http://russianidiot.github.io/images/book/16.png">
</p>
