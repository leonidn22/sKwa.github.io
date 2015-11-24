Title
#####

Subtitle
''''''''

.. contents:: Table of Contents
    :depth: 4
    :backlinks: top

Markup
======

Lists
-----

Bullet List
^^^^^^^^^^^

- first
- second
- third

Enumerated Lists
^^^^^^^^^^^^^^^^

1. first
#. second
#. third

A. first
#. second
#. third

Definition List
^^^^^^^^^^^^^^^

term 1
    Definition 1.

term 2
    Definition 2, paragraph 1.

    Definition 2, paragraph 2.

term 3 : classifier
    Definition 3.

term 4 : classifier one : classifier two
    Definition 4.


Field List
^^^^^^^^^^

    :Date: 2001-08-16
    :Version: 1
    :Authors: - Me
              - Myself
              - I
    :Indentation: Since the field marker may be quite long, the second
        and subsequent lines of the field body do not have to line up
        with the first line, but they must be indented relative to the
        field name marker, and they must line up with each other.
    :Parameter i: integer


Option List
^^^^^^^^^^^

-a          Output all.
-b          Output both (this description is
            quite long).
-c arg      Output just arg.
--long      Output all day long.

-p          This option has two paragraphs in the description.
            This is the first.

            This is the second.  Blank lines may be omitted between
            options (as above) or left in (as here and below).

--very-long-option  A VMS-style option.  Note the adjustment for
                    the required two spaces.

--an-even-longer-option
            The description can also start on the next line.

-2, --two   This option has two variants.

-f FILE, --file=FILE    These two options are synonyms; both have
                        arguments.

/V          A VMS/DOS-style option.

Tables
------

Simple Table
^^^^^^^^^^^^

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

=====  =====  ======
   Inputs     Output
------------  ------
A      B      A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

Grid Table
^^^^^^^^^^

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+

Misc
----

Footnotes
^^^^^^^^^

.. [1] Body elements go here.

Citation
^^^^^^^^

Here is a citation reference: [CIT2002]_.

.. [CIT2002] This is the citation.  It's just like a footnote,
    except the label is textual.
   

Hyperlink Targets
^^^^^^^^^^^^^^^^^

.. _hyperlink-name: link-block

Inline Literal
^^^^^^^^^^^^^^

``inline literal``

Literal Block
^^^^^^^^^^^^^

This is a typical paragraph.  An indented literal block follows.

::

    for a in [5,4,3,2,1]:   # this is program code, shown as-is
        print a
    print "it's..."
    # a literal block continues until the indentation ends

This text has returned to the indentation of the first paragraph,
is outside of the literal block, and is therefore treated as an
ordinary paragraph.

Quoted Literal Blocks
^^^^^^^^^^^^^^^^^^^^^

John Doe wrote::

>> Great idea!
>
> Why didn't I think of that?

You just did!  ;-)

Line Block
^^^^^^^^^^^

Take it away, Eric the Orchestra Leader!

    | A one, two, a one two three four
    |
    | Half a bee, philosophically,
    |     must, *ipso facto*, half not be.
    | But half the bee has got to be,
    |     *vis a vis* its entity.  D'you see?
    |
    | But can a bee be said to be
    |     or not to be an entire bee,
    |         when half the bee is not a bee,
    |             due to some ancient injury?
    |
    | Singing...

Block Quote
^^^^^^^^^^^

This is an ordinary paragraph, introducing a block quote.

    "It is my business to know things.  That is my trade."

    -- Sherlock Holmes

Doctest Block
^^^^^^^^^^^^^

This is an ordinary paragraph.

>>> print 'this is a Doctest block'
this is a Doctest block

The following is a literal block::

    >>> This is not recognized as a doctest block by
    reStructuredText.  It *will* be recognized by the doctest
    module, though!

Directives
==========

Document Parts
--------------

Section Numbering
^^^^^^^^^^^^^^^^^

.. sectnum::

Header
^^^^^^

.. header:: This is a header.

Footer
^^^^^^

.. footer:: This is a footer.


Admonitions
-----------

Attention
^^^^^^^^^

.. attention::
   Beware killer rabbits!

Caution
^^^^^^^

.. caution::
   Beware killer rabbits!

Danger
^^^^^^

.. danger::
   Beware killer rabbits!

Error
^^^^^

.. error::
   Beware killer rabbits!

Hint
^^^^

.. hint::
   Beware killer rabbits!

Important
^^^^^^^^^

.. important::
   Beware killer rabbits!

Note
^^^^

.. note::
   Beware killer rabbits!

Tip
^^^

.. tip::
   Beware killer rabbits!

Warning
^^^^^^^

.. warning::
   Beware killer rabbits!

Images
------

Image
^^^^^

.. image:: http://sphinx-doc.org/_static/sphinxheader.png

.. image:: http://sphinx-doc.org/_static/sphinxheader.png
    :height: 100px
    :width: 200 px
    :scale: 50 %
    :alt: alternate text
    :align: right

Figure
^^^^^^

.. figure:: http://sphinx-doc.org/_static/sphinxheader.png
    :scale: 50 %
    :alt: map to buried treasure

    This is the caption of the figure (a simple paragraph).

    The legend consists of all elements after the caption.  In this
    case, the legend consists of this paragraph.

Body Elements
-------------

Topic
^^^^^

.. topic:: Topic Title

    Subsequent indented lines comprise
    the body of the topic, and are
    interpreted as body elements.

Sidebar
^^^^^^^

.. sidebar:: Sidebar Title
    :subtitle: Optional Sidebar Subtitle

    Subsequent indented lines comprise
    the body of the sidebar, and are
    interpreted as body elements.

Parsed literal block
^^^^^^^^^^^^^^^^^^^^

.. parsed-literal::

    bla

Code
^^^^

.. code:: python

    def my_function():
        "just a test"
        print 8/2

Math
^^^^

.. math::

    α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)


Rubric
^^^^^^

.. rubric:: Some Heading
    
Epigraph
^^^^^^^^

.. epigraph::

    No matter where you go, there you are.

    -- Buckaroo Banzai
    
Highlights
^^^^^^^^^^

.. highlights::

    - one

    - two

    - three

Pull-Quote
^^^^^^^^^^

.. pull-quote::

    This is a pull-quote

Compound Paragraph
^^^^^^^^^^^^^^^^^^

.. compound::

    The 'rm' command is very dangerous.  If you are logged
    in as root and enter ::

        cd /
        rm -rf *

    you will erase the entire contents of your file system.

Container
^^^^^^^^^

.. container:: custom

    This paragraph might be rendered in a custom way.


Tables
------

Table
^^^^^

.. table:: Truth table for "not"

    =====  =====
    A      not A
    =====  =====
    False  True
    True   False
    =====  =====

CSV-Table
^^^^^^^^^

.. csv-table:: Frozen Delights!
    :header: "Treat", "Quantity", "Description"
    :widths: 15, 10, 30

    "Albatross", 2.99, "On a stick!"
    "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
    crunchy, now would it?"
    "Gannet Ripple", 1.99, "On a stick!"

List Table
^^^^^^^^^^

.. list-table:: Frozen Delights!
    :widths: 15 10 30
    :header-rows: 1

    * - Treat
      - Quantity
      - Description
    * - Albatross
      - 2.99
      - On a stick!
    * - Crunchy Frog
      - 1.49
      - If we took the bones out, it wouldn't be
        crunchy, now would it?
    * - Gannet Ripple
      - 1.99
      - On a stick!


References
----------

Target Footnote
^^^^^^^^^^^^^^^

.. [#some_footnote] This is a footnote

Links
^^^^^

A Link: http://www.google.com/
A Link: `Google <http://www.google.com/>`_

.. _google: http://www.google.com/

Another Link: `google`_

Misc
--------------------




And another: google2_ with a footnote: [#some_footnote]_

.. topic:: Topic Title

    Subsequent indented lines comprise
    the body of the topic, and are
    interpreted as body elements.



.. target-notes::


.. _google2: http://www.google.com/
