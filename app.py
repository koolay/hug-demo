# -*- coding: utf-8 -*-
"""
    for description
"""
import os
from os.path import join, dirname

import hug
from dotenv import load_dotenv

from modules.open import todo
from modules.backend import todo as todo_backend

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#----------- config route ---------------#
@hug.extend_api('/open')
def feature_1_modules():
    return [todo]


@hug.extend_api('/backend')
def feature_2_modules():
    return [todo_backend]

#==========================================#


import hug

@hug.get('/', versions=1)
def get_root():
  return True


if __name__ == '__main__':

    sys_name = os.environ.get('APP_NAME') # get APP_NAME from .env

