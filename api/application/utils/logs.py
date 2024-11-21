# Created at 2024/11/21 下午8:43
import logging
import os
from logging import handlers, Logger


def getLogger(name: str = 'root') -> Logger:
    """
    创建一个日志器的单例对象
    :param name: 日志器名称，默认为root
    :return: 日志器对象
    """
    logger = logging.getLogger(name)  # 创建一个日志器对象
    logger.setLevel(logging.DEBUG)  # 设置日志级别
    if not logger.handlers:  # 如果日志器没有处理器，则添加处理器
        th: logging.StreamHandler = logging.StreamHandler()  # 控制台处理器

        try:
            os.mkdir('logs')  # 创建logs文件夹
        except FileExistsError:
            pass

        rf: handlers.RotatingFileHandler = handlers.RotatingFileHandler(  # 文件处理器,按大小分割日志文件
            filename=f'logs/{name}.log',  # 日志文件名
            mode='a',
            maxBytes=300*1024*1024,  # 日志文件最大字节数
            backupCount=10,  # 日志文件备份个数
            encoding='utf-8',
        )

        # 设置每个Handler的日志等级
        th.setLevel(logging.DEBUG)
        rf.setLevel(logging.INFO)

        # 创建日志的格式器对象formatter
        simple_formatter: logging.Formatter = logging.Formatter(
            fmt="{levelname} {asctime} {pathname}:{lineno} {message}",
            style="{"
        )
        verbose_formatter: logging.Formatter = logging.Formatter(
            fmt="【{name}】{levelname} {asctime} {pathname}:{lineno} {message}",
            datefmt="%Y-%m-%d %H:%M:%S",
            style="{"
        )

        # 向Handler中添加上面创建的格式器对象
        th.setFormatter(simple_formatter)
        rf.setFormatter(verbose_formatter)

        # 将创建的Handler处理器添加到Logger日志器中
        logger.addHandler(th)
        logger.addHandler(rf)

    return logger


if __name__ == '__main__':
    logger = getLogger('dl')
    logger.info("常规运行日志")
    logger.debug("调试日志")
    logger.error("错误日志")
    logger.critical("严重错误日志")
    logger.warning("警告日志")
    logger.exception("异常日志")

