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
        MANIFEST.in

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

virtualenv
----------
http://stackoverflow.com/questions/1783146/where-in-a-virtualenv-does-my-code-go
virtualenv provides a python interpreter instance, not an application instance. You wouldn't normally create your application files within the directories containing a system's default python, likewise there's no requirement to locate your application within a virtualenv directory. For example, you might have a project where you have multiple applications using the same virtualenv. Or, you may be testing an application with a virtualenv that will later be deployed with a system python. Or, you may be packaging up a standalone app where it might make sense to have the virtualenv directory located somewhere within the app directory itself. So, in general, I don't think there is one right answer to the question. And, a good thing about virtualenv is that it supports many different use cases: there doesn't need to be one right way.
