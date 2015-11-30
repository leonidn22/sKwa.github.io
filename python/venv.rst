===================
Virtual Environment
===================



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
  - Как управлять внешними зависимостями(pyodbc => ODBCLib)?

Последний вопрос более глобальный и можно так до безконечности: "А что если 
Питон не установлен?" Как я уже упомянул, это более глобальный вопрос и им должен
заниматься администратор(sysadmin) или оператор разрботки(devop), в обязанность
которых входит об обеспечении соответствующего окружения.
