<!--
README generated with readmemako.py (github.com/russianidiot/readme-mako.py) and .README dotfiles (github.com/russianidiot-dotfiles/.README)
-->

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
