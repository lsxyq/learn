#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import sys
import PyPDF2
import PythonMagick
import ghostscript

pdffilename = r"D:\learn\5.pdf"

from wand.image import Image
from wand.color import Color

background = Color("WHITE")

with Image(filename=pdffilename, resolution=230,background=background) as img:
    img.format = 'jpeg'
    img.save(filename='converted.jpg')