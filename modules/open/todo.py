# -*- coding: utf-8 -*-
"""
    for description
"""
import hug
import falcon

from common.errors import UserError, HttpError
from services.todo_service import get_username


@hug.get('/todo/hello')
def hello(name:hug.types.text):
    name = get_username(name)
    result = {"msg": 'Welcome to module open! {}!' . format(name) }
    return result