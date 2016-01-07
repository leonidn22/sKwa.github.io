Python project structure
========================

.. contents::


Minimal
-------
::

    proj/
        proj/
            __init__.py
        setup.py

Это минимальная структура проекта на Питоне.


Basic
-----
::

    proj/
        proj/
            __init__.py
            code.py
        setup.py            # setuptools
        README.rst

Это базовая и рекомендуемая структура проекта. Так как 


Sphinx
------
::

    proj/
        docs/
            conf.py
            index.rst
        proj/
            __init__.py
            code.py
        setup.py
        README.rst
        MANIFEST.in

С Sphinx проблем нет, документация и проект две взаимосвязанные, но всё же
разные вещи. Если API(epydoc), то можно::

    proj/
        apidocs/
        docs/
            conf.py
            index.rst
        proj/
            __init__.py
            code.py
        setup.py
        README.rst
        MANIFEST.in


py.test
-------

С unit testing есть маленькая загвоздка, а где?

  - sub-module
  - separate directory

Sub-module:

  - не загрязняем пространство имён
  - таки является частью в отличии от доки

Отдельно:

  - а
  - б

::

    proj/
        utest/
            test_basic.py
            test_advanced.py
        proj/
            __init__.py
            code.py
        setup.py
        README.rst
        MANIFEST.in

Git
---
::

    proj/
        proj/
            __init__.py
            code.py
        setup.py
        README.rst
        MANIFEST.in
        .git/
        .gitignore

