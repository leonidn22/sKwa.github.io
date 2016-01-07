======
README
======

Terminology
-----------

distribution
    separately installable sets of Python modules as stored in the Python package index, 
    and installed by ``distutils`` or ``setuptools``.

package
    Python packages as defined by Python's import statement.

module
    is a file containing Python definitions and statements.

__all__
    explicit index of the package.

Layout
------
::
    mydst/
    ├── mypkg
    │   ├── __init__.py
    │   └── code.py
    ├── tests
    │   ├── __init__.py
    │   └── test_code.py
    ├── README.rst
    └── setup.py


``mydst/mypkg/__init__.py`` ::

    import code


``mydst/mypkg/code.py`` ::

    def foo(a, b, c):
        return a + b + c


``mydst/tests/test_code.py`` ::

    import mypkg
    import unittest
    
    
    class TestStringMethods(unittest.TestCase):
        def test_foo(self):
            self.assertEqual(mypkg.code.foo(1, 2, 3), 6)
    
    
    if __name__ == '__main__':
        unittest.main()


Run::

    (mydst)$ python -m unittest tests.test_code

    # or

    (mydst)$ python -m unittest discover

verbose(1)::

    $ python -m unittest -v tests.test_code
    test_foo (tests.test_code.TestStringMethods) ... ok
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s
    
    OK

verbose(2)::
    $ python -m unittest discover -v
    test_foo (tests.test_code.TestStringMethods) ... ok
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s
    
    OK


PyTest
------
https://pytest.org/latest/goodpractises.html


---
https://docs.python.org/2/tutorial/modules.html
http://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure
http://docs.python-guide.org/en/latest/writing/structure/
http://mikegrouchy.com/blog/2012/05/be-pythonic-__init__py.html
http://www.learnpython.org/en/Modules_and_Packages

https://python-packaging.readthedocs.org/en/latest/
http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/
http://infinitemonkeycorps.net/docs/pph/
