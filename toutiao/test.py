#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import requests
from hashlib import md5
"""
POST http://ntiku.api.duia.com/app/paper/list?userId=21974953&platform=2&signature=b84b093e3679659c67c0ffe1d8c2edfd&skuCode=31&appType=2&createTime=1564994155309&serialNum=1564994155309 HTTP/1.1
Host: ntiku.api.duia.com
Content-Type: application/json;charset=UTF-8
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: KJSSX/4.6.4 (iPhone; iOS 12.1.4; Scale/2.00)

{
  "d" : "-1",
  "b" : 110,
  "c" : 3,
  "a" : 31
}
"""
userId='21974953'
platform='2'

skuCode='31'
appType='2'
createTime='1564994155309'
serialNum='1564994155309'


data ={
  "d" : "-1",
  "b" : 110,
  "c" : 3,
  "a" : 31
}



md = md5()
md.update(userId.encode('utf8'))
md.update(platform.encode('utf8'))
md.update(skuCode.encode('utf8'))
md.update(appType.encode('utf8'))
md.update(createTime.encode('utf8'))
md.update(serialNum.encode('utf8'))
md.update(str(data).encode('utf8'))

signature='b84b093e3679659c67c0ffe1d8c2edfd'

print(md.hexdigest(),'\t',signature)
