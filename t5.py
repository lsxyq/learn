#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import requests

headers = {
    "filetype": "mp4",
    "filesize": "12980",
    "access_token": "sdfsdfsdfsd",
}

res = requests.get("http://upload.iqiyi.com/openupload/", headers=headers)
print(res.content)

data = {
    "code": "A00000",
    "data": {
        "upload_url": "http://220.181.184.157/upload",
        "file_id": "4004551398f84a38a371e107f099d27e"}
}

# data 中的 file_id 用于后续上传标识文件
# data 中的 upload_url 作为后续上传文件时 POST 的地址
