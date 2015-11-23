===
VIM
===


Remove unwanted empty lines::

    :g/^$/d
    :v/./d
    :g/^\s*$/d


Delete all lines that are empty or that contain only whitespace characters (spaces, tabs)::

    :g/^\s*$/d
    :v/\S/d

Delete all trailing whitespace::

    :%s/\s\+$//e
    :%s/\n\{3,}/\r\r/e

CJK (Chinese, Japanese, Korean)::

    :g/^[ \t\u3000]*$/d
