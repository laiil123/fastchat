# Created at 2024/11/21 下午6:26
import os
import uvicorn
from application import create_app, FastAPI

app: FastAPI = create_app()


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=os.environ.get('APP_HOST', '127.0.0.1'),
        port=int(os.environ.get('APP_PORT', 8000)),
        reload=bool(os.environ.get('APP_RELOAD', 'True'))
    )

