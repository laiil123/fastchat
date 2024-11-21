# Created at 2024/11/21 下午6:31
import os

from fastapi import FastAPI
from dotenv import load_dotenv
from tortoise.contrib.fastapi import register_tortoise

from . import settings
from .apps.common.views import app as common_app
from .apps.users.views import app as users_app
from .utils import middleware, exceptions


def create_app() -> FastAPI:
    """工厂函数：创建App对象"""
    load_dotenv()  # 加载环境变量
    app: FastAPI = FastAPI(
        title=os.environ.get('APP_NAME', 'fastchat'),
        summary=os.environ.get('APP_SUMMARY', 'fastchat'),
        description=os.environ.get('APP_DESCRIPTION', 'fastchat'),
        version=os.environ.get('APP_VERSION', '1.0.0'),
        exception_handlers={  # 注册全局异常处理
            exceptions.HTTPException: exceptions.global_http_exception_handler,
            exceptions.RequestValidationError: exceptions.global_request_exception_handler,
        }
    )

    register_tortoise(  # 注册Tortoise-ORM
        app,
        config=settings.TORTOISE_ORM,
        generate_schemas=False,  # 是否自动创建表
        add_exception_handlers=True,  # 是否添加异常处理
    )
    # 注册各个分组应用中的视图接口代码到App对象中
    app.include_router(common_app)  # 添加路由
    app.include_router(users_app, prefix='/users')  # 添加路由

    # 注册中间件函数
    http_middleware = app.middleware('http')
    http_middleware(middleware.log_requests)

    return app
