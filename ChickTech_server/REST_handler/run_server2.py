from REST_handler import UserHandler

__author__ = 'Nafisa'
from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import json
from DB_handler.db_methods import DBManager


class UserHandler2(tornado.web.RequestHandler):
    def get(self):
        response = {'Received': 'GET'}
        self.write(response)

    def post(self, *args, **kwargs):
        try:
            body = self.request.body.decode("utf-8")
            jsonbody = json.loads(body)
            profile = jsonbody.get("data").get("profile")
            manager = DBManager()
            manager.insertProfile(profile)
            response = {'Received': profile}
            self.write(response)
        except Exception as ex:
            self.write({"error": "error happened"})




application = tornado.web.Application([
    (r"/user", UserHandler2)
    # (r"/user", UserHandler)

])

if __name__ == "__main__":
    application.listen(9000)
    tornado.ioloop.IOLoop.instance().start()