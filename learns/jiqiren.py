#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import arrow
import itchat
import pydash
import requests


def local_datetime():
    """格式化的时间戳"""
    return arrow.now().format("YYYY-MM-DD HH:mm:ss")


def get_user_info(wx_msg):
    """获取发送信息的用户参数"""
    userName = wx_msg['FromUserName']
    data = itchat.search_friends(userName=userName)
    info = pydash.pick(data, 'UserName', 'NickName', 'RemarkName', 'Signature')
    return info


def get_response(wx_msg):
    """处理接受到的信息，调用机器人接口回复消息"""
    user_info = get_user_info(wx_msg)
    message = wx_msg["Text"]
    print('来至{}\t{}\t{}'.format(user_info.get('RemarkName'), message, local_datetime()))
    reply = access_ownthink_robot(message)
    print('回复{}\t{}\t{}'.format(user_info.get('RemarkName'), reply, local_datetime()))
    return reply


def access_ownthink_robot(message):
    """调用思知机器人回复消息
    origin='https://www.ownthink.com/'
    :param message:
    :return:
    """
    url = "https://api.ownthink.com/bot?appid=07b27cd71c9137c494a874d0afa34f8d&spoken={}".format(message)
    r = requests.get(url)
    reply = pydash.get(r.json(), 'data.info.text')
    return reply


def access_tuling_robot(message):
    """调用图灵机器人回复消息
    {
    "intent": {
        "code": 10005,
        "intentName": "",
        "actionName": "",
        "parameters": {
            "nearby_place": "酒店"
        }
    },
    "results": [
        {
         	"groupType": 1,
            "resultType": "url",
            "values": {
                "url": "http://m.elong.com/hotel/0101/nlist/#indate=2016-12-10&outdate=2016-12-11&keywords=%E4%BF%A1%E6%81%AF%E8%B7%AF"
            }
        },
        {
         	"groupType": 1,
            "resultType": "text",
            "values": {
                "text": "亲，已帮你找到相关酒店信息"
            }
        }
        ]
    }
    :param message:
    :return:
    """
    # origin="http://openapi.tuling123.com/"
    url = "http://openapi.tuling123.com/openapi/api/v2"
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": message,
            },
        },
        "userInfo": {
            "apiKey": "c2591a4b447844cdb1d57e0a69fe6154",
            "userId": "dongting"
        }
    }
    r = requests.post(url, json=data)
    reply = pydash.get(r.json(), 'results.values.text')
    return reply


@itchat.msg_register(itchat.content.TEXT)
def text_reply(wx_msg):
    """接受微信消息并回复"""
    return get_response(wx_msg)


if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()
