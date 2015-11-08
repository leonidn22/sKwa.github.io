============================
Пишем RESTful API на Торнадо
============================

The Tornado Web framework makes it easy to write RESTful APIs in Python. How easy? Have a look

Торнадо Веб Фреймворк позволит вам очен' легко создават' RESTfull API на Питоне. Как легко? Сам посмотри как легко.

---


Tornado is a Python Web framework and asynchronous networking library that provides excellent scalability due to its non-blocking network I/O. It also greatly facilitates building a RESTful API quickly. These features are central to Tornado, as it is the open-source version of FriendFeed's Web server. A few weeks ago, Tornado 3.  was released, and it introduced many improvements. In this article, I show how to build a RESTful API with the latest Tornado Web framework and I illustrate how to take advantage of its asynchronous features.

::

    #!/usr/bin/env python
    # coding: utf-8
    """DEMO"""
    
    import tornado.escape
    import tornado.ioloop
    import tornado.web
    from datetime import date
    
    
    class VersionHandler(tornado.web.RequestHandler):
        def get(self):
            response = {'version': '3.5.1', 'last_build': date.today().isoformat()}
            self.write(response)
    
    
    class GetGameByIdHandler(tornado.web.RequestHandler):
        def get(self, id):
            response = {
                'id': int(id),
                'name': 'Crazy Game',
                'release_date': date.today().isoformat()
            }
            self.write(response)
    
    
    if __name__ == "__main__":
        application = tornado.web.Application([
            (r"/getgamebyid/([0-9]+)", GetGameByIdHandler),
            (r"/version", VersionHandler)
        ])
        application.listen(8080)
        tornado.ioloop.IOLoop.instance().start()
