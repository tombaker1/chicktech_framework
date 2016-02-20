from tornado import web
from tornado import gen

__author__ = 'Nafisa'

class UserHandler(web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(UserHandler, self).__init__(application, request, **kwargs)

    @gen.coroutine
    @web.asynchronous
    def post(self):
        print("received post request")
