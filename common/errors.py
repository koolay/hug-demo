# -*- coding: utf-8 -*-
"""
    Errors
"""
import falcon


class Error(BaseException): pass # 错误基类


class UserError(Error):
    def __init__(self, code, message):
        """
        业务异常基类, 返回message给用户
        :param int code:
        :param str message:
        """
        self.code = code
        self.message = message


class HttpError(falcon.HTTPError):
    """
    http异常类类, 需要返回http status
    """
    def __init__(self, status, message=None, code=None):
        super(HttpError, self).__init__(status=status, title='HTTPError', description=message, code=code)


class InvalidArgumentError(UserError): pass # 无效参数异常


class ServerError(HttpError):
    """
    程序逻辑或意外未捕获的未知异常
    """
    def __init__(self):
        super(ServerError, self).__init__(500, falcon.HTTP_500)
