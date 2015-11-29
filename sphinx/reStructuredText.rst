================
reStructuredText
================

H\ :sub:`2`\ O

E = mc\ :sup:`2`

:title-reference:World

.. contents:: `Table of contents`
   :depth: 1
   :local:


.. topic:: Заголовок

    Привет Мир!

.. rubric:: Моя рубрика


In line
--------

.. If you use sphinx there are also three predefined substitutions: |title|.

Table
~~~~~

+--------------------+-------------------------------+--------------------+
| Plaintext          | HTML                          | Browser            |
+====================+===============================+====================+
| \*emphasis\*       | <em>emphasis</em>             | *emphasis*         |
+--------------------+-------------------------------+--------------------+
| \**strong\**       | <strong>strong</strong>       | **strong**         |
+--------------------+-------------------------------+--------------------+
| \`interpreted\`    | <cite>interpreted</cite>      | `interpreted`      |
+--------------------+-------------------------------+--------------------+
| \``inline\``       | <tt class="docutils literal">\| ``inline``         |
|                    | inline</tt>                   |                    |
+--------------------+-------------------------------+--------------------+


Container
---------

.. container:: myclass

   There is also a general ...


Code
----

.. code-block:: ruby
    
    puts('Hello')


.. code:: python
   :number-lines: 2
    
    import sys
    script, args = sys.argv[0], sys.argv[1:]
    print 'Script name:', script
    print 'Script args:', args


.. code:: c
    
    int sum(int x, int y){
        return x + y;
    }


.. code:: sh
   :class: foobar
   :name: eggbaz
   :number-lines: 2

    for FILE in ./*; do echo "${FILE}"; done


http://docutils.sourceforge.net/docs/index.html

----

[#] An Introduction to reStructuredText
[#] reStructuredText Markup Specification
[#] reStructuredText Directives
[#] reStructuredText Interpreted Text Roles
[#] reStructuredText Standard Definition Files

