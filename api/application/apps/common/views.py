# Created at 2024/11/21 下午7:33
from fastapi import APIRouter, HTTPException

app = APIRouter()


@app.get('/api')
async def api() -> dict:
    return {'title': 'fastchat api'}


@app.get('/exception')
async def exception(name: str) -> dict:
    try:
        print(username)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'name': name}

