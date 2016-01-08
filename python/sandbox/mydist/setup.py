#/usr/bin/env python
# coding: utf-8
"""An example of ``setup.py`` file.

Install::

    $ python setup.py develop

Uninstall::

    $ python setup.py develop --uninstall

"""
import os
import setuptools

import mypackage

# global variables
CWD = os.path.abspath(os.path.dirname(__file__))


def get_description():
    """\
    Function Docstring
    ------------------

    Extracts README.rst content.
    """
    readme_file = os.path.join(CWD, 'README.rst')
    with open(readme_file, 'r') as file_descriptor:
        return file_descriptor.read()


setuptools.setup(
    name="mypackage",     # `name` as package dir ???
    version=mypackage.__version__,
    packages=setuptools.find_packages(),
    author=mypackage.__author__,
    author_email='foobar@example.com',
    description=mypackage.__doc__,
    url="www.example.com",
    long_description=get_description(),
    license='GPLv3',
    platforms='Platform Independent', )
