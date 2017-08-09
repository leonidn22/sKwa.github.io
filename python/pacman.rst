===================================
Software Packaging and Distribution
===================================

https://docs.python.org/2/distutils/examples.html


Что нужно понимать:

  • repository root dir
  • project root dir

Other docs
----------

  • http://www.kennethreitz.org/essays/repository-structure-and-python
  • http://python-packaging.readthedocs.org/en/latest/index.html
  • http://intermediate-and-advanced-software-carpentry.readthedocs.org/en/latest/structuring-python.html
  • http://hmarr.com/2010/jan/19/making-virtualenv-play-nice-with-git/
  • https://packaging.python.org/en/latest/distributing/
  • http://www.ewencp.org/blog/a-brief-introduction-to-packaging-python/
  • https://mail.python.org/pipermail/python-list/2013-November/661175.html
  • https://blog.ionelmc.ro/2014/05/25/python-packaging/
  • https://docs.pytest.org/en/latest/goodpractices.html
  • https://blog.ionelmc.ro/2014/06/25/python-packaging-pitfalls/



Packages:

  • ``distutils``
  • ``ensurepip``


.. contents::


Building and Distributing Packages with Setuptools
--------------------------------------------------

Project minimal structure
~~~~~~~~~~~~~~~~~~~~~~~~~
http://packaging.python.org/en/latest/distributing/
https://github.com/pypa/sampleproject
::

    calc/
        [bin/]
        [lib/]
        calc/
            __init__.py
            code.py
        [data/]
        [docs/]
        [tests/]
        setup.py
        README.rst
        [setup.cfg]
        [MANIFEST.in]
        [ tox.ini]
        [.gitignore]
        [.travis.yml]


.. code:: python
    # setup.py
    from setuptools import setup, find_packages

    setup(
        name='calc',
        version='0.1',
        packages = find_packages(),
    )


.. code:: python

    #!/usr/bin/env python
    # coding: utf-8
    # file  : code.py

    try:
        while True:
            expression = raw_input('%> ')
            print eval(expression)
    except:
        print 'error => exit'

Now we can install the package locally (for use on our system), with::

    $ python setup.py install
    # or
    $ python setup.py develop


Итог: минимальная структура проекта на Питоне

Better Package
~~~~~~~~~~~~~~

``README.rst`` + ``MANIFEST.in`` added::

    calc/
        calc/
            __init__.py
        setup.py
        README.rst
        MANIFEST.in
        requirements.txt


Sphinx
~~~~~~
::

    calc/
        docs/
            conf.py
            index.rst
        calc/
            __init__.py
            calc.py
        setup.py
        README.rst
        MANIFEST.in
        requirements.txt

Git
~~~
::

    calc/
        docs/
            conf.py
            index.rst
        calc/
            __init__.py
            calc.py
        setup.py
        README.rst
        MANIFEST.in
        requirements.txt
        .gitignore


Unit Test
~~~~~~~~~


2 options:

  • package level
  • as sub-module of package

in case it's on package level test modules must import your packaged module to test it. You can do this a few ways:

  • Expect the package to be installed in site-packages.
  • Use a simple (but explicit) path modification to resolve the package properly.

I highly recommend the latter.
To give the individual tests import context, create a tests/context.py file

.. code:: python
    import os
    import sys
    sys.path.insert(0, os.path.abspath('..'))


.. code:: python
    calc/
        docs/
            conf.py
            index.rst
        test/
            test_basic.py
            test_advanced.py
        calc/
            __init__.py
            calc.py
        setup.py
        README.rst
        MANIFEST.in
        requirements.txt
        .gitignore


Distributing Python Modules
https://docs.python.org/2/distutils/index.html

Installing Python Modules
https://docs.python.org/2/install/index.html
