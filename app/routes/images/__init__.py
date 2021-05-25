from fastapi import APIRouter
from fastapi.responses import Response

from .pillow import *

router = APIRouter()

@router.get("/image/cmm")
async def changemymind(text : str):
    buffer = await cmm(text)
    return Response(buffer.getvalue())


@router.get("/image/thisisfine")
async def tif(text : str):
    buffer = await thisisfine(text)
    return Response(buffer.getvalue())

@router.get("/image/court")
async def court(text : str):
    buffer = await objection(text)
    return Response(buffer.getvalue())