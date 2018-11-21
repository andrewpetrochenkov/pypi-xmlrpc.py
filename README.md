[![](https://img.shields.io/pypi/pyversions/pypi-xmlrpc.svg?longCache=True)](https://pypi.org/pypi/pypi-xmlrpc/)
[![](https://img.shields.io/pypi/v/pypi-xmlrpc.svg?maxAge=3600)](https://pypi.org/pypi/pypi-xmlrpc/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/pypi-xmlrpc.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/pypi-xmlrpc.py/)

#### Install
```bash
$ [sudo] pip install pypi-xmlrpc
```

#### Functions
function|description
-|-
`pypi_xmlrpc.list_packages()`|return list of all server packages
`pypi_xmlrpc.package_releases(name, show_hidden=True)`|return list of package releases
`pypi_xmlrpc.package_roles(name)`|return list of package roles
`pypi_xmlrpc.release_data(name, version)`|return dictionary with release data
`pypi_xmlrpc.release_urls(name, version)`|return list of release urls
`pypi_xmlrpc.user_packages(user)`|return list of user packages

#### CLI
usage|description
-|-
`python -m pypi_xmlrpc.package_releases name`|print package releases
`python -m pypi_xmlrpc.user_packages user`|print user packages

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

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>