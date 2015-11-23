	
Install
'''''''

github.com_: :code:`pip install git+git://github.com/b'russianidiot'/pypixmlrpc.py.git`

pypi.python.org_: :code:`pip install pypixmlrpc`

download_: :code:`python setup.py install` or :code:`setup/.setup.py develop.command`

.. _github.com: http://github.com/b'russianidiot'/pypixmlrpc.py
.. _pypi.python.org: https://pypi.python.org/pypi/pypixmlrpc
.. _download: https://github.com/b'russianidiot'/pypixmlrpc.py/archive/master.zip

	

	

	

Usage 
'''''
.. code-block::

	from pypixmlrpc import *

	pypi.list_packages()

	pypi.user_packages("kennethreitz")

	pypi.package_releases("requests")

	pypi.package_roles("requests")

	version="x.y.z"
	pypi.release_data("requests",version)
	pypi.release_downloads("requests",version)
	pypi.release_urls("requests",version)

------------

**Tested**: python 2.6, 2.7, 3+

**Bug Tracker**: `github.com/b'russianidiot'/pypixmlrpc.py/issues`__

__ https://github.com/b'russianidiot'/pypixmlrpc.py/issues