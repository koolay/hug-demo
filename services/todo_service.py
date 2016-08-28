# -*- coding: utf-8 -*-
"""
    for description
"""
import logging

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

    return username.upper()
