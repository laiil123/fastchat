# Created at 2024/11/21 下午9:07
import os
import time

from .logs import getLogger


async def log_requests(request, call_next):
    """
    日志中间件
    :param request: HTTP请求对象
    :param call_next: 调用下一个中间件或路由
    :return:
    """
    logger = getLogger(os.environ.get('APP_NAME', 'root'))
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000  # 毫秒
    formatted_process_time = '{0:.2f}'.format(process_time)  # 保留两位小数
    logger.info(f'path={request.url.path} status_code={response.status_code} timer={formatted_process_time}ms')  # 记录日志

    return response
