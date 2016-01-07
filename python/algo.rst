Algorithms
==========


Graphs and Trees
----------------

Binary Tree Class::

    class Node(object):
        def __init__(self, left, right):
            self.left = left
            self.right = right

Multiway Tree Class::

   class Node(object):
        def __init__(self, kids, next=None)
            self.kids = kids
            self.next = next

The Bunch PATTERN::

    class Bunch(object):
        def __init__(self, *args, **kwargs):
            super(Bunch, self).__init__(*args, **kwargs)
            self.__dict__ = self
 
Counting
~~~~~~~~
::

    >>> S, x = range(1, 67), 13
    >>> x * sum(S) == sum((x * y) for y in S)
    True

Recursion and Reduction
~~~~~~~~~~~~~~~~~~~~~~~
...


  - http://interactivepython.org/courselib/static/pythonds/index.html
  - https://www.quora.com/Whats-a-good-algorithms-book-with-examples-in-Python
  - http://legacy.python.org/workshops/2002-02/papers/15/index.htm
  - https://github.com/nryoung/algorithms



TITLE   : Introduction to Algorithms, 3rd Edition
YEAR    : 2009
AUTHOR  : Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein
ISBN-13 : 978-0262033848
ISBN-10 : 0262033844 


TITLE   : Problem Solving with Algorithms and Data Structures Using Python
YAER    : 2015
AUTHOR  : Miller, Bradley N., Ranum, David L.
ISBN-13 : 978-1590280539
ISBN-10 : 1590280539 


TITLE   : Python Algorithms: Mastering Basic Algorithms in the Python Language
YEAR    : 2010
AUTHOR  : Magnus Lie Hetland
ISBN-13 : 978-1430232377
ISBN-10 : 1430232374


TITLE   : Working with Algorithms in Python
YEAR    : 2104
AUTHOR  : George T. Heineman
ISBN-13 : 978-1491907818

TITLE   : Data Structures and Algorithms in Python
YEAR    : 2003
AUTHOR  : Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser
ISBN-13 : 978-1118549582
ISBN-10 : 1118549589


TITLE   :
YEAR    :
AUTHOR  :
ISBN-13 :
ISBN-10 :

Longest Common Substring Algorithm
  - http://www.bogotobogo.com/python/python_longest_common_substring_lcs_algorithm_generalized_suffix_tree.php
  - http://www.algorithmist.com/index.php/Longest_Common_Subsequence
  - https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_subsequence#Python
  - http://rosettacode.org/wiki/Longest_common_subsequence#Python
  - https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
