<p align="center">
	<b>pypi XML-RPC wrapper</b>
</p>

[![Build Status](https://travis-ci.org/russianidiot/pypixmlrpc.py.svg?branch=master)](https://travis-ci.org/russianidiot/pypixmlrpc.py)[![PyPI](https://img.shields.io/pypi/v/pypixmlrpc.svg)](https://pypi.python.org/pypi/pypixmlrpc)
[![PyPI](https://img.shields.io/pypi/pyversions/pypixmlrpc.svg)](https://pypi.python.org/pypi/pypixmlrpc)[![PyPI](https://img.shields.io/pypi/dm/pypixmlrpc.svg)](https://pypi.python.org/pypi/pypixmlrpc)[![PyPI](https://img.shields.io/pypi/dw/pypixmlrpc.svg)](https://pypi.python.org/pypi/pypixmlrpc)[![PyPI](https://img.shields.io/pypi/dd/pypixmlrpc.svg)](https://pypi.python.org/pypi/pypixmlrpc)

	
Install
-------

[github.com](http://github.com/russianidiot/pypixmlrpc.py):
`pip install git+git://github.com/russianidiot/pypixmlrpc.py.git`

[pypi.python.org](https://pypi.python.org): `pip install pypixmlrpc`

[download](https://github.com/russianidiot/pypixmlrpc.py/archive/master.zip): `python setup.py install` or `setup/.setup.py develop.command` 

	

	

Usage 
=====
```
from pypixmlrpc import *

pypi.list_packages()

pypi.user_packages("kennethreitz")

pypi.package_releases("requests")

pypi.package_roles("requests")

version="x.y.z"
pypi.release_data("requests",version)
pypi.release_downloads("requests",version)
pypi.release_urls("requests",version)
```

---

Feedback 
--------

[![GitHub issues](https://img.shields.io/github/issues/russianidiot/pypixmlrpc.py.svg)](https://github.com/russianidiot/pypixmlrpc.py/issues) - Github Issues

[![Join the chat at https://gitter.im/russianidiot/pypixmlrpc.py](https://badges.gitter.im/russianidiot/pypixmlrpc.py.svg)](https://gitter.im/russianidiot/pypixmlrpc.py) - **Chat** with me (english/russian) 

---

<p align="center">
my Python packages <a href="http://russianidiot.github.io/python/">russianidiot.github.io/python/</a>
<img src="http://russianidiot.github.io/images/python/16.png" />
</p>

<p align="center">
	all my repos <a href="http://russianidiot.github.io/">russianidiot.github.io</a> <img src="http://russianidiot.github.io/images/star/16.png" />
</p>

<p align="center">
	follow me <a href="http://github.com/russianidiot">github.com/russianidiot</a>
<img src="http://russianidiot.github.io/images/github/16.png" />
</p>

<p align="center">
	README.md generated with <a href="https://github.com/russianidiot-dotfiles/.README">.README</a> (python+mako, sh)
<img src="http://russianidiot.github.io/images/book/16.png">
</p>