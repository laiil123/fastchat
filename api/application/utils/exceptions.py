# Created at 2024/11/21 下午9:23
import os
from fastapi import Request, status
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse

from .logs import getLogger

logger = getLogger(os.environ.get('APP_NAME', 'root'))


def global_http_exception_handler(request: Request, exc):
    """
    全局HTTP请求异常处理
    :param request: HTTP请求对象
    :param exc: 本次发生的异常对象
    :return:
    """
    logger.error(f"发生异常：{exc.detail}")

    return JSONResponse({
        'code': exc.status_code,
        'err_msg': exc.detail,
        'status': 'Failed'
    })


def global_request_exception_handler(request: Request, exc):
    """
    全局请求校验异常处理
    :param request: HTTP请求对象
    :param exc: 本次发生的异常对象
    :return:
    """
    return JSONResponse({
        'code': status.HTTP_400_BAD_REQUEST,
        'err_msg': exc.errors()[0],  # 获取第一个错误信息
        'status': 'Failed'
    })
