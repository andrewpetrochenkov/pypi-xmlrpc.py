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