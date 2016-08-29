# -*- coding: utf-8 -*-
"""
    for description
"""
import logging

from dao.todo_dao import get_app_by_id

logger = logging.getLogger(__name__)


def get_username(username):
    """
    get username
    :param username:
    :return:
    """
    logger.info('get username')
    logger.debug('get username')
    logger.warning('get username')
    row = get_app_by_id('39d7b8d2-5667-dfb1-a4f3-b483e551a811')
    logger.info(row)
    return username.upper()
