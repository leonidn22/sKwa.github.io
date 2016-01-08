===================
Virtual Environment
===================

* virtualenv
* virtualenvwrapper

``virtualenv`` - is a tool to create isolated Python environments(Project X 
depends on libFoo-v1.x and Project Y depends on libFoo-v2.x).

``virtualenvwrapper`` - wrappers for creating and deleting virtual environments
and otherwise managing your development workflow.


What is your virtualenv, git, pip, ..., development flow?
---------------------------------------------------------
https://www.reddit.com/r/Python/comments/1ia8r1/what_is_your_virtualenv_git_pip_development_flow/

Дискуссия на Reddit

.. code:: bash

    $ mkvirtualenv foo
    $ git clone ssh://foo
    $ cd foo
    $ pip install -r requirements.txt
    $ python foo.py
    
    $ cd ../bar
    $ workon bar
    $ python bar.py

Я попробовал этот способ и у меня не получилось: падало на команде 
``git clone <url>`` с ошибкой, что такая директория уже существует.

.. code:: bash

    $ git clone <url> <dir>
    $ virtualenv <dir>
    $ cd <dir>
    $ source bin/activate

it will create a next structure::

    project-name/
        bin/
        include/
        lib/
        local/
        project-name/
            module/
                __init__.py
                module.py
                ...
            setup.cfg
            setup.py

Once in the ``virtualenv``, I install my dependencies with ``pip``, either
manually or with a ``requirements.txt``.

Disatvantage: same path for virtual environment and Python package.

Легитимные вопросы на которые надо дать ответ:

  - А что если я захочу папку ``bin/`` или ``lib/``?
  - Как определить и управлять репозиторием при использовании СКВ(git, к примеру)?
  - Как управлять внешними зависимостями(pyodbc зависит от unixODBC)?

Последний вопрос более глобальный и можно так до безконечности: "А что если 
Питон не установлен?" Как я уже упомянул, это более глобальный вопрос и им должен
заниматься администратор(sysadmin) или оператор разрботки(devop), в обязанность
которых входит об обеспечении соответствующего окружения.

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
- Why I hate virtualenv and pip
https://pythonrants.wordpress.com/2013/12/06/why-i-hate-virtualenv-and-pip/

- What is your virtualenv, git, pip, ..., development flow?
https://www.reddit.com/r/Python/comments/1ia8r1/what_is_your_virtualenv_git_pip_development_flow/

- The Hitchhiker’s Guide to Python! Virtualenv
http://docs.python-guide.org/en/latest/dev/virtualenvs/

- Archlinux Virtualenv
https://wiki.archlinux.org/index.php/Python/Virtualenv


