import os

from PIL import Image
import uuid
from test_task import settings


def create_watermarked_picture(image):
    image = Image.open(image)
    watermark = Image.open(settings.MEDIA_ROOT + '/assets/Sample-Watermark-Transparent.png')
    filename = f'{uuid.uuid4()}.png'
    width, height = image.size
    resized_watermark = watermark.resize((width, height), Image.ANTIALIAS)
    transparent_image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent_image.paste(image, (0, 0))
    transparent_image.paste(resized_watermark, (0, 0), mask=resized_watermark)
    transparent_image.save(os.path.join(settings.MEDIA_ROOT, filename))
    return filename
