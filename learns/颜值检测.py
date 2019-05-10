#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import time
import pydash
import base64
import requests
from lxml import etree
from aip import AipFace
from pathlib import Path

# 百度云 人脸检测 申请信息
# 唯一必须填的信息就这三行
APP_ID = "15793380"
API_KEY = "aClspWsLfxELstGxnFYEPSjq"
SECRET_KEY = "oLKUE8liCG7A1LnrEjyGyR2XRg3prMHL"
# 文件存放目录名，相对于当前目录
DIR = "image"
# 过滤颜值阈值，存储空间大的请随意
BEAUTY_THRESHOLD = 55
# 如果权限错误，浏览器中打开知乎，在开发者工具复制一个，无需登录
# 建议最好换一个，因为不知道知乎的反爬虫策略，如果太多人用同一个，可能会影响程序运行
# 如何替换该值下文有讲述
AUTHORIZATION = "oauth c3cef7c66a1843f8b3a9e6a1e3160e20"

# 以下皆无需改动
# 每次请求知乎的讨论列表长度，不建议设定太长，注意节操
LIMIT = 5

# 这是话题『美女』的 ID，其是『颜值』（20013528）的父话题
SOURCE = "19552207"

# 爬虫假装下正常浏览器请求
USER_AGENT = "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.5 Safari/534.55.3"
# 爬虫假下正常浏览器请求
REFERER = "https://www.zhihu.com/topic/%s/newest" % SOURCE
# 某话题下讨论列表请求 url
BASE_URL = "https://www.zhihu.com/api/v4/topics/%s/feeds/timeline_activity"
# 初始请求 url 附带的请求参数
URL_QUERY = "?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.comment_count&limit=" + str(
    LIMIT)

HEADERS = {
    "User-Agent": USER_AGENT,
    "Referer": REFERER,
    "authorization": AUTHORIZATION
}


# 指定 url，获取对应原始内容 / 图片
def fetch_image(url):
    try:
        response = requests.get(url, headers=HEADERS)
    except Exception as e:
        raise e
    return response.content


# 指定 url，获取对应 JSON 返回 / 话题列表
def fetch_activities(url):
    try:
        response = requests.get(url, headers=HEADERS)
    except Exception as e:
        raise e
    return response.json()


# 处理返回的话题列表
def parser_activities(datums, face_detective):
    for data in datums["data"]:
        target = data["target"]
        if "content" not in target or "question" not in target or "author" not in target:
            continue
        html = etree.HTML(target["content"])
        seq = 0
        title = target["question"]["title"]
        author = target["author"]["name"]
        images = html.xpath("//img/@src")
        for image in images:
            if not image.startswith("http"):
                continue
            image_data = fetch_image(image)
            score = face_detective(image_data)
            if not score:
                continue
            name = "{}--{}--{}--{}.jpg".format(score, author, title, seq)
            seq = seq + 1
            path = Path(__file__).parent.joinpath("image").joinpath(name)
            try:
                f = open(path, "wb")
                f.write(image_data)
                f.flush()
                f.close()
                print(path)
                time.sleep(2)
            except Exception as e:
                continue

    if not datums["paging"]["is_end"]:
        return datums["paging"]["next"]
    else:
        return None


def init_detective(app_id, api_key, secret_key):
    client = AipFace(app_id, api_key, secret_key)
    options = {"face_field": "age,gender,beauty,qualities"}

    def detective(image):
        image = str(base64.b64encode(image), "utf-8")
        response = client.detect(str(image), "BASE64", options)
        response = response.get("result")
        if not response:
            return
        if (not response) or (response["face_num"] == 0):
            return
        face_list = response["face_list"]
        if pydash.get(face_list, "0.face_probability") < 0.6:
            return
        if pydash.get(face_list, "0.beauty") < BEAUTY_THRESHOLD:
            return
        if pydash.get(face_list, "0.gender.type") != "female":
            return
        score = pydash.get(face_list, "0.beauty")
        return score

    return detective


def main():
    face_detective = init_detective(APP_ID, API_KEY, SECRET_KEY)
    url = BASE_URL % SOURCE + URL_QUERY
    while url is not None:
        datums = fetch_activities(url)
        url = parser_activities(datums, face_detective)
        time.sleep(5)


if __name__ == '__main__':
    main()


"""
##导入相关包
```
import time
import pydash
import base64
import requests
from lxml import etree
from aip import AipFace
from pathlib import Path
```
##百度云 人脸检测 申请信息
```
#唯一必须填的信息就这三行
APP_ID = "15793380"
API_KEY = "aClspWsLfxELstGxnFYEPSjq"
SECRET_KEY = "oLKUE8liCG7A1LnrEjyGyR2XRg3prMHL"
# 过滤颜值阈值，存储空间大的请随意
BEAUTY_THRESHOLD = 55
```
```
AUTHORIZATION = "oauth c3cef7c66a1843f8b3a9e6a1e3160e20"
# 如果权限错误，浏览器中打开知乎，在开发者工具复制一个，无需登录
# 建议最好换一个，因为不知道知乎的反爬虫策略，如果太多人用同一个，可能会影响程序运行
# 如何替换该值下文有讲述
```
##以下皆无需改动
```
# 每次请求知乎的讨论列表长度，不建议设定太长，注意节操
LIMIT = 5
# 这是话题『美女』的 ID，其是『颜值』（20013528）的父话题
SOURCE = "19552207"
```
##爬虫假装下正常浏览器请求
```
USER_AGENT = "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.5 Safari/534.55.3"
REFERER = "https://www.zhihu.com/topic/%s/newest" % SOURCE
# 某话题下讨论列表请求 url
BASE_URL = "https://www.zhihu.com/api/v4/topics/%s/feeds/timeline_activity"
# 初始请求 url 附带的请求参数
URL_QUERY = "?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.comment_count&limit=" + str(
    LIMIT)

HEADERS = {
    "User-Agent": USER_AGENT,
    "Referer": REFERER,
    "authorization": AUTHORIZATION
}
```
##指定 url，获取对应原始内容 / 图片
```
def fetch_image(url):
    try:
        response = requests.get(url, headers=HEADERS)
    except Exception as e:
        raise e
    return response.content
```
##指定 url，获取对应 JSON 返回 / 话题列表
```
def fetch_activities(url):
    try:
        response = requests.get(url, headers=HEADERS)
    except Exception as e:
        raise e
    return response.json()
```

##处理返回的话题列表
```
def parser_activities(datums, face_detective):
    for data in datums["data"]:
        target = data["target"]
        if "content" not in target or "question" not in target or "author" not in target:
            continue
        html = etree.HTML(target["content"])
        seq = 0
        title = target["question"]["title"]
        author = target["author"]["name"]
        images = html.xpath("//img/@src")
        for image in images:
            if not image.startswith("http"):
                continue
            image_data = fetch_image(image)
            score = face_detective(image_data)
            if not score:
                continue
            name = "{}--{}--{}--{}.jpg".format(score, author, title, seq)
            seq = seq + 1
            path = Path(__file__).parent.joinpath("image").joinpath(name)
            try:
                f = open(path, "wb")
                f.write(image_data)
                f.flush()
                f.close()
                print(path)
                time.sleep(2)
            except Exception as e:
                continue

    if not datums["paging"]["is_end"]:
        return datums["paging"]["next"]
    else:
        return None
```
##初始化颜值检测工具
```
def init_detective(app_id, api_key, secret_key):
    client = AipFace(app_id, api_key, secret_key)
    options = {"face_field": "age,gender,beauty,qualities"}

    def detective(image):
        image = str(base64.b64encode(image), "utf-8")
        response = client.detect(str(image), "BASE64", options)
        response = response.get("result")
        if not response:
            return
        if (not response) or (response["face_num"] == 0):
            return
        face_list = response["face_list"]
        if pydash.get(face_list, "0.face_probability") < 0.6:
            return
        if pydash.get(face_list, "0.beauty") < BEAUTY_THRESHOLD:
            return
        if pydash.get(face_list, "0.gender.type") != "female":
            return
        score = pydash.get(face_list, "0.beauty")
        return score

    return detective
```
##程序入口
```
def main():
    face_detective = init_detective(APP_ID, API_KEY, SECRET_KEY)
    url = BASE_URL % SOURCE + URL_QUERY
    while url is not None:
        datums = fetch_activities(url)
        url = parser_activities(datums, face_detective)
        time.sleep(5)

if __name__ == '__main__':
    main()
```
"""
