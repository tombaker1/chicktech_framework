from REST_handler import UserHandler

__author__ = 'Nafisa'
from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import json
from DB_handler.db_methods import DBManager


def modify(profiles):
    for profile in profiles:
        del profile["_id"]
    return profiles



class UserHandler2(tornado.web.RequestHandler):
    def get(self):
        query = self.request.query
        manager = DBManager()
        if query != "":
            list = query.split("=")
            dict = {list[0]:list[1]}
            profiles = manager.listDesiredProfiles(dict)
        else:
            profiles = manager.listProfiles()


        modified_profiles = modify(profiles)
        response = json.dumps(modified_profiles)

        self.write(response)

    def post(self, *args, **kwargs):
        try:
            body = self.request.body.decode("utf-8")
            jsonbody = json.loads(body)
            profile = jsonbody.get("data").get("profile")
            manager = DBManager()
            manager.insertProfile(profile)
            # response = json.dumps(profile)
            response = {'message': 'Data was inserted Successfully'}
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