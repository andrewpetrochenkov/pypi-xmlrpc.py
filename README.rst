.. image:: https://img.shields.io/pypi/v/pypixmlrpc.svg
   :target: https://pypi.python.org/pypi/pypixmlrpc

.. image:: https://img.shields.io/pypi/pyversions/pypixmlrpc.svg
   :target: https://pypi.python.org/pypi/pypixmlrpc

.. image:: https://img.shields.io/pypi/dm/pypixmlrpc.svg
   :target: https://pypi.python.org/pypi/pypixmlrpc

	

Install
~~~~~~~

github.com_: :code:`pip install git+git://github.com/russianidiot/pypixmlrpc.py.git`

pypi.python.org_: :code:`pip install pypixmlrpc`

download_: :code:`[ -e requirements.txt ] && pip install -r requirements.txt; python setup.py install`

.. _github.com: http://github.com/russianidiot/pypixmlrpc.py
.. _pypi.python.org: https://pypi.python.org/pypi/pypixmlrpc.py
.. _download: https://github.com/russianidiot/pypixmlrpc.py/archive/master.zip

	

	

	

Usage
~~~~~

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

----

Feedback
~~~~~~~~

|github_issues| - Github Issues

.. |github_issues| image:: https://img.shields.io/github/issues/russianidiot/pypixmlrpc.py.svg
	:target: https://github.com/russianidiot/pypixmlrpc.py/issues

|gitter| - **Chat** with me (english/russian) 

.. |gitter| image:: https://badges.gitter.im/russianidiot/pypixmlrpc.py.svg
	:target: https://gitter.im/russianidiot/pypixmlrpc.py

`russianidiot.github.io/python/`_  - my Python packages

.. _russianidiot.github.io/python/: http://russianidiot.github.io/python/