.. image:: https://img.shields.io/badge/language-python-blue.svg

.. image:: https://img.shields.io/pypi/pyversions/pypixmlrpc.svg
   :target: https://pypi.python.org/pypi/pypixmlrpc

|codacy| |landscape| |codeclimate| |scrutinizer|

.. |scrutinizer| image:: https://scrutinizer-ci.com/g/russianidiot/pypixmlrpc.py/badges/quality-score.png?b=master
   :target: https://scrutinizer-ci.com/g/russianidiot/pypixmlrpc.py/master
   :alt: scrutinizer-ci.com

.. |codacy| image:: https://img.shields.io/codacy/2d0aefd518834ab49eb01c0d475fcef9.svg
   :target: https://www.codacy.com/app/russianidiot-github/pypixmlrpc-py/dashboard
   :alt: codacy.com

.. |codeclimate| image:: https://img.shields.io/codeclimate/github/russianidiot/pypixmlrpc.py.svg
   :target: https://codeclimate.com/github/russianidiot/pypixmlrpc.py
   :alt: codeclimate.com

.. |landscape| image:: https://landscape.io/github/russianidiot/pypixmlrpc.py/master/landscape.svg?style=flat
   :target: https://landscape.io/github/russianidiot/pypixmlrpc.py/master
   :alt: landscape.io

Install
```````

:code:`[sudo] pip install pypixmlrpc`

Usage
`````
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

Sources:

*	`py_modules/pypixmlrpc.py`_

.. _`py_modules/pypixmlrpc.py`: https://github.com/russianidiot/pypixmlrpc.py/blob/master/py_modules/pypixmlrpc.py

Feedback |github_issues| |gitter| |github_follow|

.. |github_issues| image:: https://img.shields.io/github/issues/russianidiot/pypixmlrpc.py.svg
	:target: https://github.com/russianidiot/pypixmlrpc.py/issues

.. |github_follow| image:: https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow
	:target: https://github.com/russianidiot

.. |gitter| image:: https://badges.gitter.im/russianidiot/pypixmlrpc.py.svg
	:target: https://gitter.im/russianidiot/pypixmlrpc.py

----

`russianidiot.github.io/python/`_  - Python packages

.. _russianidiot.github.io/python/: http://russianidiot.github.io/python/

`russianidiot.github.io/cli/`_  - command line scripts

.. _russianidiot.github.io/cli/: http://russianidiot.github.io/cli/

`README.rst`_  - generated with `readmemako.py`_ (python+ `mako`_ templates) and `.README`_ dotfiles

.. _README.rst: https://github.com/russianidiot/pypixmlrpc.py/blob/master/README.rst
.. _readmemako.py: http://github.com/russianidiot/readmemako.py/
.. _mako: http://www.makotemplates.org/
.. _.README: https://github.com/russianidiot-dotfiles/.README
