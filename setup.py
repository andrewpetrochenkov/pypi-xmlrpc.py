import setuptools

setuptools.setup(
    name='pypi-xmlrpc',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
