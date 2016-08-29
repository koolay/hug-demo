# -*- coding: utf-8 -*-
"""
    for description
"""
from dao.simplemysql import get_db


def get_app_by_id(id):

    with get_db() as db:
        return db.query('SELECT name,id FROM app WHERE `id`=%s', id)
