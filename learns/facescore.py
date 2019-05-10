import time
import os
import re
import pydash
import base64
from aip import AipFace

APP_ID = "15793380"
API_KEY = "aClspWsLfxELstGxnFYEPSjq"
SECRET_KEY = "oLKUE8liCG7A1LnrEjyGyR2XRg3prMHL"

options = {"face_field": "age,gender,beauty,qualities"}


def init_client(app_id, api_key, secret_key):
    client = AipFace(app_id, api_key, secret_key)
    return client


def detective(image, options):
    client = init_client(APP_ID, API_KEY, SECRET_KEY)
    image = str(base64.b64encode(image), "utf-8")
    response = client.detect(str(image), "BASE64", options)
    response = response.get("result")
    print(response)


image = open("D:\learn\image\80--然新--你见过哪些惊为天人的人间绝色？要区别于一般美女或帅哥的？--0.jpg", "rb").read()

detective(image, options)
