from fastapi import FastAPI
import aiohttp
import asyncio


app = FastAPI(debug = True)
app.session = aiohttp.ClientSession()


@app.get("/")
async def home():
    return {
        "msg" : "Hello"
    }












