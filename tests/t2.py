#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import threading
from pathlib import Path

import pythoncom
from win32com import client

path = [r'C:\Projects\learn\ppt\3\测试教案.pptx', r'C:\Projects\learn\ppt\2\工作总结PPT模板.ppt']


def convert(path):
    pythoncom.CoInitialize()
    handler = client.Dispatch("PowerPoint.Application")
    ppt = handler.Presentations.Open(path, True, False, False)
    pages = ppt.Slides.Count
    list_image(Path(path).parent, pages)
    ppt.SaveAs(Path(path).parent, 17)


for i in path:
    thread = threading.Thread(
        target=convert,
        args=(i,)
    )
    thread.start()


def image(path, pages):
    has_list = []
    while True:
        for i in Path(path).iterdir():
            if i.as_posix() in has_list: continue
            print(path, i.as_posix())
            has_list.append(i.as_posix())
        if len(has_list) == pages: break


def list_image(path, pages):
    thread = threading.Thread(
        target=image,
        args=(path, pages)
    )
    thread.start()
