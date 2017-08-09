Celery
======

* `Очередь сообщений и асинхронные задачи с помощью Celery и RabbitMQ <http://devacademy.ru/posts/ochered-soobschenij-i-asinhronnyie-zadachi-s-pomoschyu-celery-i-rabbitmq/>`_

::

    clr
    ├── __init__.py
    ├── celery.py
    └── tasks.py


http://docs.celeryproject.org/en/latest/getting-started/next-steps.html#next-steps


``celery.py``::

    from __future__ import absolute_import, print_function, unicode_literals
    from celery import Celery

    app = Celery('clr', backend='rpc://', broker='pyamqp://', include=['clr.tasks'])

    # Optional configuration, see the application user guide.
    app.conf.update(result_expires=3600,)


    if __name__ == '__main__':
        app.start()


``tasks.py``::

    from __future__ import absolute_import, print_function, unicode_literals
    from .celery import app

    @app.task
    def add(x, y):
        return x + y

    @app.task
    def mul(x, y):
        return x * y

    @app.task
    def xsum(numbers):
        return sum(numbers)
