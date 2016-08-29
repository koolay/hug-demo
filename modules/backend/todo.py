# -*- coding: utf-8 -*-
"""
    for description
"""
import hug

from services.todo_service import get_username


@hug.get('/backend/hello')
def hello(name:hug.types.text):

    name = get_username(name)
    return 'Hello, welcome backend! {}!' . format(name)