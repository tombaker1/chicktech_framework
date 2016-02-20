from REST_handler import UserHandler

__author__ = 'Nafisa'

from tornado import web


APPLICATION = web.Application(
    [
        (r'.*/v1/token/?$', UserHandler)
    ])