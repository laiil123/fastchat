# Created at 2024/11/21 下午7:33
from fastapi import APIRouter

app = APIRouter()


@app.get('/login')
async def login():
    return {'method': 'login'}