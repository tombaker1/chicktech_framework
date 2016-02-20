from REST_handler import UserHandler

__author__ = 'Nafisa'
from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web

class UserHandler2(tornado.web.RequestHandler):
    def get(self):
        response = { 'version': '3.5.1',
                     'last_build':  date.today().isoformat() }
        self.write(response)


application = tornado.web.Application([
    (r"/user", UserHandler2)
    # (r"/user", UserHandler)

])

if __name__ == "__main__":
    application.listen(9000)
    tornado.ioloop.IOLoop.instance().start()