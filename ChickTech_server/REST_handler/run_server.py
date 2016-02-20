import sys
from tornado import ioloop
from REST_handler import UserHandler

__author__ = 'Nafisa'

from tornado import web


APPLICATION = web.Application(
    [
        # (r'.*/v1/token/?$', UserHandler)
        (r'.*/v1/token/?$', UserHandler)
    ])


if __name__ == '__main__':
    PORT = 9000
    APPLICATION.listen(PORT)
    print(PORT)

    ioloop.IOLoop.current().start()
