===
Git
===

.. contents::


Введение
--------

Цели
    Что он из себя представляет(GIT - контроль версий)?

История
    Что, зачем и почему? (если есть и другие продукты). СКВ против ЦСКВ


Настройка Git
-------------

Три вида настроек:

  • системные          --system  (``/etc/gitconfig``)
  • пользовательские   --global  (``${HOME}/.gitconfig``)
  • локальные          --local   (``${REPO}/.git/config``)

настройки пользователя::

    $ git config --global user.name "<user>"
    $ git config --global user.email "<email>"

настройки редактора::

    $ git config --global core.editor vim
    $ git config --global merge.tool vimdiff

Проверка настроек::

    $ git config --list

Проверка настроек по ключу::

    $ git config <key>
    $ git config user.name



Основы Git
----------

Создание Git-репозитория
~~~~~~~~~~~~~~~~~~~~~~~~

Клонирование существующего репозитория::

    $ git clone <repository>

Создание репозитория в существующем каталоге::

    $ git init

Привязка к удалённому репозиторию::

    $ git remote add origin <url>

Привязка к удалённому репозиторию нужна, когда используются Git-хостинг сервис.
Хорошо мы создали и пользуем репозиторий локально и теперь надо и другим дать
доступ к нашим разработкам. Вот для этого мы и делаем "привязку".


Git-хостинг
-----------

GitHub
~~~~~~
...


BitBucket
~~~~~~~~~
...


GitLab
~~~~~~
...


References
----------
- https://git-scm.com/
- https://git-scm.com/book/en/v2
- https://github.com/
- https://bitbucket.org/
- https://gitlab.com/
