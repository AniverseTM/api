from PIL import Image
from io import BytesIO
from app.utils.decorators import *



@with_executor()
def spank(io_1 : BytesIO, io_2 : BytesIO):
    image_1 = Image.open(io_1)
    image_2 = Image.open(io_2)