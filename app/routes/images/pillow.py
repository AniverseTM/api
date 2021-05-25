from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import textwrap
from app.utils.decorators import *

# font ttf file from: https://fontsfree.net/sf-pro-display-regular-font-download.html


@with_executor
def cmm(text : str) -> BytesIO:
    text = textwrap.wrap(text, width = 30)
    text = "\n".join(text)
    base = Image.open("./app/assets/images/cmmbase.png")
    font = ImageFont.truetype("./app/assets/fonts/base.ttf", 45)
    base_draw = ImageDraw.Draw(base)
    base_draw.multiline_text((268, 627), text, (0, 0, 0), font = font)
    buffer = BytesIO()
    base.save(buffer, format = "PNG")
    buffer.seek(0)
    return buffer


@with_executor
def thisisfine(text : str) -> BytesIO:
    text = textwrap.wrap(text, width = 37)
    text = "\n".join(text)
    base = Image.open("./app/assets/images/thisisfine.png")
    font = ImageFont.truetype("./app/assets/fonts/base.ttf", 45)
    base_draw = ImageDraw.Draw(base)
    base_draw.multiline_text((29, 28), text, (0, 0, 0), font = font)
    buffer = BytesIO()
    base.save(buffer, format = "PNG")
    buffer.seek(0)
    return buffer

@with_executor
def objection(text : str) -> BytesIO:
    text = textwrap.wrap(text, width = 37)
    text = "\n".join(text)
    base = Image.open("./app/assets/images/court.png")
    font = ImageFont.truetype("./app/assets/fonts/base.ttf", 45)
    base_draw = ImageDraw.Draw(base)
    base_draw.multiline_text((37, 502), text, (255, 255, 255), font = font)
    buffer = BytesIO()
    base.save(buffer, format = "PNG")
    buffer.seek(0)
    return buffer

