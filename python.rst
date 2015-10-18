======
Python
======

5 different methods to use an else block in python
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



