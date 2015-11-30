========================
Python project structure
========================



- :emphasis:`emphasis`
- :literal:`literal`
- :code:`code`
- :math:`E_org = mc^2`
- :math:`H_2O`
- H\ :sub:`2`\ O
- 2\ :sup:`3`\ = 8
- :strong:`strong`
- See :PEP:`287` for more information.
- See :RFC:`2822` for information about email headers.
- hello :title-reference:`XXX\ *foo*\ **bar**`


.. contents::


:title-reference:`hello`
Lorem ist ipsum. Image is a strong picture.


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
        setup.py
        README.rst
        MANIFEST.in

Это базовая и рекомендуемая структура проекта.


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


env vcs tst doc 
 0   0   0   0  | V
 0   1   0   0  | V
 0   1   1   0  | V
 0   1   1   1  | V
 1   1   0   0  | X

:title-reference:foo bar
egg spamm
