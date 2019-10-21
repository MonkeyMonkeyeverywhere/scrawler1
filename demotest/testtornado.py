import tornado
from tornado.web import RequestHandler


class MainHandler(RequestHandler):
    def get(self):
        self.write("hello tornado")


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler)
    ])


if 1:
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
