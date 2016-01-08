#!/usr/bin/env python
# coding: utf-8


def hello(name=None):
    """
    Dummy function.

    >>> hello()
    'Helo Stranger!'
    >>> hello('John')
    'Hello John!'
    """
    name = name or 'Stranger'
    return 'Hello %s!' % (name, )


if __name__ == '__main__':
    print hello()
