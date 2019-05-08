#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
# compress_image
# click-> dosomething
import json
from io import BytesIO

import pydash
from tempfile import TemporaryFile

import requests
from PIL import Image
r = requests.get("https://imglive.ehafo.com/course/temp/2019/03/eqxocp2LhcCrgBtN0hTBsVm5zm2gpFTFZPhKUhd4.png")
fd = BytesIO(r.content)
width, height = Image.open(fd,'r').size
print(width,height)
