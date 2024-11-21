# Created at 2024/11/21 下午7:10
import os

TORTOISE_ORM = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': os.environ.get('DB_HOST', '127.0.0.1'),
                'port': int(os.environ.get('DB_PORT', 3306)),
                'user': os.environ.get('DB_USER', 'root'),
                'password': os.environ.get('DB_PASSWORD', 'czh031016'),
                'database': os.environ.get('DB_NAME', 'fastchat'),
                'charset': os.environ.get('DB_CHARSET', 'utf8mb4'),
                'minsize': int(os.environ.get('DB_POOL_MINSIZE', 1)),
                'maxsize': int(os.environ.get('DB_POOL_MAXSIZE', 5)),
                'echo': bool(os.environ.get('APP_DEBUG', True))
            }
        }
    },
    'apps': {
        'models': {
            'models': ['application.apps.users.models', 'aerich.models'],
            'default_connection': 'default'
        }
    },
    'use_tz': False,
    'timezone': os.environ.get('APP_TIMEZONE', 'Asia/Shanghai')
}
