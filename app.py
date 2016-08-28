# -*- coding: utf-8 -*-
"""
    for description
"""
import os
from os.path import join, dirname

import hug
from dotenv import load_dotenv

from common.errors import UserError, ServerError, HttpError
from modules.open import todo
from modules.backend import todo as todo_backend

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


# ----------- handlers --------------------#

@hug.not_found(output=hug.output_format.text)
def not_found():
    return 'Not Found'


@hug.exception(hug.falcon.HTTPError)
def http_error_handle(exception, response):
    response.status = exception.status
    response.content_type = 'text/plain'
    return exception.description


@hug.exception(UserError)
def user_error_handle(exception, response):
    response.status = hug.falcon.HTTP_200
    return {'errcode': exception.code, 'errmsg': exception.message}


@hug.exception(BaseException)
def user_error_handle(exception, response):
    response.status = 500
    response.content_type = 'text/plain'
    return exception.description

# ----------- config route ---------------#


@hug.extend_api('/open')
def feature_1_modules():
    return [todo]


@hug.extend_api('/backend')
def feature_2_modules():
    return [todo_backend]

# ==========================================#


if __name__ == '__main__':
    sys_name = os.environ.get('APP_NAME')  # get APP_NAME from .env
