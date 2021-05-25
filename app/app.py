from fastapi import FastAPI
import aiohttp
import asyncio

# routers
from app.routes import images

app = FastAPI(debug = True)
app.include_router(images.router)
app.session = aiohttp.ClientSession()


@app.get("/")
async def home():
    return {
        "msg" : "Hello"
    }












