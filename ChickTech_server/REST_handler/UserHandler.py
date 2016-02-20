from tornado import web
from tornado import gen

__author__ = 'Nafisa'

class UserHandler(web.RequestHandler):
    # def __init__(self, application, request, **kwargs):
    #     super(UserHandler, self).__init__(application, request, **kwargs)

    # @gen.coroutine
    # @web.asynchronous
    def post(self):
        try:
            print("received post request")
            body = self.request
            response = {'data': 'value'}
            self.write(response)
        except Exception as ex:
            self.write("exception occurred.")

    def get(self):
        response = { 'version': '3.5.1' }
        self.write(response)