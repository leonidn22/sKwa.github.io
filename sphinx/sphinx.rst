======
Sphinx
======


Документация бывает разная:
  - научная: словарь, учебник, медицинская
  - производственная: бланки
  - техническая: патенты,

Как пример можно взять `RFC www.rfc-editor.org`

RFC, EPub, XML, PDF, Doc, ReST

Markup language
https://en.wikipedia.org/wiki/Markup_language

Lightweight markup language
https://en.wikipedia.org/wiki/Lightweight_markup_language

reStructuredText
https://en.wikipedia.org/wiki/ReStructuredText

Sphinx
https://en.wikipedia.org/wiki/Sphinx_%28documentation_generator%29

Documentation generator
https://en.wikipedia.org/wiki/Documentation_generator

Software documentation
https://en.wikipedia.org/wiki/Software_documentation

Documentation
https://en.wikipedia.org/wiki/Documentation

Docutils
http://docutils.sourceforge.net/

Проследить за историей развития можно из PEP-обсуждений:

    * 216 - Docstring Format                        Rejected
    * 224 - Attribute Docstrings                    Rejected
    * 256 - Docstring Processing System Framework   Rejected
    * 257 - Docstring Conventions                   Active
    * 258 - Docutils Design Specification           Rejected
    * 287 - reStructuredText Docstring Format       Active

более интересный документ - PEP 287, он определяет цели и т.п.

Goals
-----

These are the generally accepted goals for a docstring format, as discussed in the Doc-SIG:

    - It must be readable in source form by the casual observer.
    - It must be easy to type with any standard text editor.
    - It must not need to contain information which can be deduced from parsing the module.
    - It must contain sufficient information (structure) so it can be converted to any reasonable markup format.
    - It must be possible to write a module's entire documentation in docstrings, without feeling hampered by the markup language.

reStructuredText meets and exceeds all of these goals, and sets its own goals as well, even more stringent. See Docstring-Significant Features below. 

- http://rst.ninjs.org/
- https://www.blender.org/manual/preferences/themes.html
- http://wiki.blender.org/index.php/Doc:2.4/Manual


Conventions
-----------
    - All modules should normally have docstrings.
    - All functions and classes exported by a module should also have docstrings.
    - A package may be documented in the module docstring of the __init__.py file in the package directory.
    - For consistency, always use """triple double quotes""" around docstrings.
    - There are two forms of docstrings: one-liners and multi-line docstrings.





Intro
-----

Для начала надо понять какие цели преследует Sphinx или его разработчики:

    **Purpose and Function**

    Sphinx converts reStructuredText files into HTML websites and other formats
    including PDF, EPub and man.
    ...
    reStructuredText is extensible, and Sphinx exploits its extensible nature
    through a number of extensions --- for autogenerating documentation from 
    source code, writing mathematical notation or highlighting source code, etc.
    ...
    Sphinx — это генератор документации, который преобразует файлы в формате 
    reStructuredText в HTML website и другие форматы (PDF, EPub и man).


т.е. основная цель Sphinx`а --- это конвертация файлов в формате reStructuredText
в другие форматы, такие как ``tex``, ``ebub``, ``html``. 

Хорошо, если основная цель Sphinx`a это конвертация reStructuredText в другие
форматы, то надо понять что из себя представляет reStructuredText.

    **reStructuredText**

    is a file format for textual data used primarily in the Python programming
    language community for technical documentation.
    ...
    In this sense, reStructuredText is a lightweight markup language designed to
    be both (a) processable by documentation-processing software such as Docutils,
    and (b) easily readable by human programmers who are reading and writing Python
    source code.
    ...
    облегчённый язык разметки, хорошо применим для создания простых веб-страниц и
    других документов, а также в качестве вспомогательного языка при написанииэ
    комментариев в программном коде.

Что это такое мы уже поняли - reStructuredText это "облегчённый язык разметки".
Но если честно, то не совсем понятно, надо разобраться что-же имеется ввиду под 
понятием - "облегчённый язык разметки" и можно двигаться далее.

    **Облегчённые языки разметки**

    Языки, предназначенные для простого и быстрого написания текста в простом
    текстовом редакторе, называются облегчёнными. Особенности таких языков:
      - Минимум функций.
      - Небольшой набор поддерживаемых тегов.
      - Легки в освоении.
      - Исходный текст на таком языке читается с такой же лёгкостью, как и готовый
        документ.
    

    **Язы́к разме́тки**

    набор символов или последовательностей, вставляемых в текст для передачи
    информации о его выводе или строении.

Вот блин... эта песня не нова начинай сначала...

    **reStructuredText** 

    is plaintext that uses simple and intuitive constructs to indicate the structure 
    of a document.

Намного лучше :) то есть reStructuredText - это открытый, нешифрованный текст,
который использует простые и интуитивные блоки для индикации структуры текста.
Я верю в простые вещи и если ТЫ не можешь просто объяснить/описать вещь/объект/явление,
то скорее всего нету полного понимания той вещи/объекта/явления.



Prerequisites
-------------
  - Python (>=2.6) or (>=3.3)
  - docutils
  - Jinja2
  - Pygments (optional)


Quick Start::

    $ sphinx-quickstart

Running the build::

    $ sphinx-build -b html <sourcedir> <builddir>
    $ make html


Glossary
--------
  - source directory
  - master document
  - conf.py
  - indext.rst


source directory:

  The root directory of a Sphinx collection of reStructuredText document
  sources is called the source directory. This directory also contains the
  Sphinx configuration file conf.py, where you can configure all aspects
  of how Sphinx reads your sources and builds your documentation.

master document:
