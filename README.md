<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/pypi-xmlrpc.svg?longCache=True)](https://pypi.org/project/pypi-xmlrpc/)
[![](https://img.shields.io/pypi/v/pypi-xmlrpc.svg?maxAge=3600)](https://pypi.org/project/pypi-xmlrpc/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/pypi-xmlrpc.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/pypi-xmlrpc.py/)

#### Installation
```bash
$ [sudo] pip install pypi-xmlrpc
```

#### Functions
function|`__doc__`
-|-
`pypi_xmlrpc.list_packages()` |return a list of all server packages
`pypi_xmlrpc.package_roles(name)` |return a list of package roles
`pypi_xmlrpc.release_data(name, version)` |return dictionary with release data
`pypi_xmlrpc.release_urls(name, version)` |return a list of release urls

#### Executable modules
usage|`__doc__`
-|-
`python -m pypi_xmlrpc.package_releases name` |print package releases
`python -m pypi_xmlrpc.user_packages user` |print user packages

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
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>