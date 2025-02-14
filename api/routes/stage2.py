from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

app = APIRouter()

@app.get('/stage2')
async def stage2():
    return {'message' : 'welcome to stage 2'}
