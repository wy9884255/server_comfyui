#public Utilities funciton
from io import BytesIO
import base64
from PIL import Image
import numpy as np
import cv2
import urllib
import datetime

#device id served
INSTANT_ID_DEV = [
    '192.168.2.231:8001'
]
INPAINTING_DEV = [
    '192.168.2.231:8101'
]

class ImageUtils:

    @classmethod
    def pil_base64(self, img, coding='utf-8'):
        img_format = img.format
        if img_format == None:
            img_format = 'JPEG'
    
        format_str = 'JPEG'
        if 'png' == img_format.lower():
            format_str = 'PNG'
        if 'gif' == img_format.lower():
            format_str = 'gif'
    
        if img.mode == "P":
            img = img.convert('RGB')
        if img.mode == "RGBA":
            format_str = 'PNG'
            img_format = 'PNG'
    
        output_buffer = BytesIO()
        img.save(output_buffer, quality=100, format=format_str)
        byte_data = output_buffer.getvalue()
        base64_str = base64.b64encode(byte_data).decode(coding)
        return base64_str
    
    @classmethod
    def base64_to_pil(self, base64_str, coding='utf-8'):
        byte_data = base64.b64decode(base64_str.encode(coding))
        image_data = BytesIO(byte_data)
        pil_image = Image.open(image_data)
        return pil_image
    
    @classmethod
    def base64_to_cv_image(self, base64_string):
        image_bytes = base64.b64decode(base64_string)
        np_array = np.frombuffer(image_bytes, np.uint8)
        cv_image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        return cv_image
    
    @classmethod
    def readImageFromUrl(self, url):
        import ssl
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        req = urllib.request.urlopen(url, context=context)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        retval, buffer = cv2.imencode('.jpg', img)
        b64img = base64.b64encode(buffer).decode("utf-8")
        return b64img
    
    @classmethod
    def resize_image(self, image, max_size):
        width, height = image.size
        if width > height:
            new_width = max_size
            new_height = int(height * max_size / width)
        else:
            new_width = int(width * max_size / height)
            new_height = max_size
        resized_image = image.resize((new_width, new_height))
        return resized_image
    
    @classmethod
    def concatenate_images(self, image1, image2):
        width1, height1 = image1.size
        width2, height2 = image2.size
        concatenated_width = width1 + width2
        concatenated_height = max(height1, height2)
        concatenated_image = Image.new('RGB', (concatenated_width, concatenated_height))
        concatenated_image.paste(image1, (0, 0))
        concatenated_image.paste(image2, (width1, 0))
        return concatenated_image
