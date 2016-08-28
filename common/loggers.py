# -*- coding: utf-8 -*-
"""
    for description
"""

import logging
import os

from raven import Client

def init_logging():

    _level = os.environ.get('APP_LOG_LEVEL')
    _handlers = os.environ.get('APP_LOG_HANDLER')

    _verbose_fmt = logging.Formatter('%(levelname)s %(asctime)s %(filename)s[line:%(lineno)d] %(message)s')
    _simple_fmt = logging.Formatter('%(levelname)s %(asctime)s %(message)s')

    _file_handler = logging.FileHandler('runtime/log/app.log')
    _file_handler.setLevel(_level)
    _file_handler.setFormatter(_verbose_fmt)

    _console_handler = logging.StreamHandler()
    _console_handler.setFormatter(_simple_fmt)
    _console_handler.setLevel(_level)

    logging.basicConfig(level=_level)
    _logger = logging.getLogger()

    if 'file' in _handlers.split(','):
        _logger.addHandler(_file_handler)

#
# class SentryLoggingHandler(LoggingHandler):
#
#     def __init__(self, dsn=None):
#
#         super(SentryLoggingHandler, self).__init__()
#
#         self.dsn = dsn
#         self.client = Client(dsn=dsn)
#
#     def capture(self):
#         self.client.captureException()


