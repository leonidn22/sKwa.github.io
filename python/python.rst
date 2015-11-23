======
Python
======

OnLine IDE
http://code.runnable.com/

Beginner’s guide to Web Scraping in Python (using BeautifulSoup)
http://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/?utm_content=buffer65241&utm_medium=social&utm_source=plus.google.com&utm_campaign=buffer

WSGI
https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface
http://wsgi.tutorial.codepoint.net/
https://www.python.org/dev/peps/pep-0333/
http://docs.repoze.org/moonshining/pep333.html
http://blog.dscpl.com.au/2009/09/roadmap-for-python-wsgi-specification.html


Books
-----
http://wombat.org.ua/AByteOfPython/toc.html


Python Project the Right Way
----------------------------
- https://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
- http://www.pydanny.com/cookie-project-templates-made-easy.html


EAFP
----

http://programmers.stackexchange.com/questions/175655/python-forgiveness-vs-permission-and-duck-typing

Easier to ask for forgiveness than permission. This common Python coding style
assumes the existence of valid keys or attributes and catches exceptions if the
assumption proves false. This clean and fast style is characterized by the 
presence of many try and except statements. The technique contrasts with the 
LBYL style common to many other languages such as C.




5 different methods to use an else block in python
--------------------------------------------------

http://www.idiotinside.com/2015/10/18/5-methods-to-use-else-block-in-python/


*Method 1*
::
    x = True
    
    if x:
        print 'x is true'
    else:
        print 'x is not true'


*Method 2*
::
    mark = 40
    is_pass = True if mark >= 50 else False
    print "Pass? " + str(is_pass)


*Method 3*
::
    for i in range(10):
        print i
    else:
        print 'For loop completed the execution'


*Method 4*
::
    for i in range(10):
        print i
        if i == 5:
            break
    else:
        print 'For loop completed the execution'


*Method 5*
::
    a = 0
    loop = 0
    while a <= 10:
        print a
        loop += 1
        a += 1
    else:
        print "While loop execution completed"



A non-magical introduction to Pip and Virtualenv for Python beginners
http://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/

Virtualenv, Virtualenvwrapper and Pip - A python newbie's best friends 
http://2buntu.com/articles/1450/virtualenv-virtualenvwrapper-and-pip-a-python-newbies-best-friends/

Python Web-based Serial Console using WebSockets
http://fabacademy.org/archives/2015/doc/WebSocketConsole.html

Adding Non-Code Files
http://python-packaging.readthedocs.org/en/latest/non-code-files.html

Packaging and Distributing Projects
https://packaging.python.org/en/latest/distributing/

Building and Distributing Packages with Setuptools
https://pythonhosted.org/setuptools/setuptools.html

A Brief Introduction to Packaging Python
http://www.ewencp.org/blog/a-brief-introduction-to-packaging-python/


