from fastapi import FastAPI
from starlette.types import Message 

app = FastAPI()

@app.get('/')

async def root():
    return {"a": "Hoang dep trai"}