distname.py/
distname.py/py_modules/modname.py
distname.py/packages/pkgname/__init__.py


python setup.py build
   ./build/
   ./build/lib/modname.py
   ./build/lib/pkgname/

python setup.py develop: (setuptools required)
  site-packages/distname.egg-link

python setup.py install:
	Python 2.x:
   	site-packages/pkgname.egg (distutils, setuptools)
 		python setup.py install --old-and-unmanageable:
  	site-packages/pkgname.egg-info, site-packages/pkgname.py
  	Python 3.x:
   	site-packages/modname.py, site-packages/modname.egg-info (distutils - default)
   	site-packages/modname.egg (setuptools)

python setup.py install --old-and-unmanageable (Python 2.x only)
  site-packages/distname.egg-info
  	site-packages/modname.py
 	site-packages/pkgname/

python setup.py install_egg_info (setuptools):
	site-packages/distname.egg-info

python setup.py install_egg_info (setuptools):
	site-packages/distname.egg-info

python setup.py install_lib:
	site-packages/modname.py
	site-packages/pkgname/

python setup.py install_scripts:
	/usr/local/bin/scriptname

# python setup.py register
#   pypi.python.org/distname

# python setup.py sdist
#   ./dist/distname-x.y.z.tar.gz

# python setup.py test (setuptools)

# python setup.py upload


