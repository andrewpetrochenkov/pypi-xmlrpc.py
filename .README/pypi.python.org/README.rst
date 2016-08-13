.. README generated with readmemako.py (github.com/russianidiot/readme-mako.py) and .README dotfiles (github.com/russianidiot-dotfiles/.README)

Install
```````

:code:`[sudo] pip install pypixmlrpc`

.. code-block:: python

	>>> from pypixmlrpc import *

	>>> pypi.list_packages()

	>>> pypi.user_packages("kennethreitz") # user packages

	>>> pypi.package_releases("requests")

	>>> pypi.package_roles("requests")

	>>> version="x.y.z"
	>>> pypi.release_data("requests",version)
	>>> pypi.release_downloads("requests",version)
	>>> pypi.release_urls("requests",version)

`Examples/`_

.. _Examples/: https://github.com/russianidiot/pypixmlrpc.py/tree/master/Examples

Feedback |github_issues| |gitter| |github_follow|

.. |github_issues| image:: https://img.shields.io/github/issues/russianidiot/pypixmlrpc.py.svg
	:target: https://github.com/russianidiot/pypixmlrpc.py/issues

.. |github_follow| image:: https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow
	:target: https://github.com/russianidiot

.. |gitter| image:: https://badges.gitter.im/russianidiot/pypixmlrpc.py.svg
	:target: https://gitter.im/russianidiot/pypixmlrpc.py
