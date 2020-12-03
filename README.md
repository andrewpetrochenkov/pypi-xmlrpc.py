<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/pypi-xmlrpc.svg?maxAge=3600)](https://pypi.org/project/pypi-xmlrpc/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/pypi-xmlrpc.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/pypi-xmlrpc.py/actions)

### Installation
```bash
$ [sudo] pip install pypi-xmlrpc
```

#### Examples
`user_packages(user)` `[(role,name),...]`
```python
>>> packages = pypi_xmlrpc.user_packages("kennethreitz") # user packages
>>> for role, name in packages:
```

`package_releases(name)`
```python
>>> pypi_xmlrpc.package_releases("requests")
['x.y.z',..., '0.0.1']
```

`package_roles(name)` `[(role,name),...]`
```python
>>> pypi_xmlrpc.package_roles("requests")
[('role','username'),...]
```

`release_data(name,version)`
```python
>>> pypi_xmlrpc.release_data("requests","x.y.z")
{'name': 'requests',...}
```


`release_urls(name,version)`
```python
>>> pypi_xmlrpc.release_urls("requests","x.y.z")
[...]
```

#### Links
+   [PyPiXmlRpc - PythonInfo Wiki](http://wiki.python.org/moin/PyPiXmlRpc)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
