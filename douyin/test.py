#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import requests

# url = 'http://v9-dy-y.ixigua.com/bb849a4baea5191c4f60401bc078b565/5d2eee10/video/m/2200d095224f6de4a45b6b5fb4f5104dfe81162dec2500002e30f33bef99/?rc=M3Ntamd5cGU3bjMzNmkzM0ApQHRAbzc5PDY0NDU0NDM3OTo6PDNAKXUpQGczdSlAZjN2KUBmbGRqZXpoaGRmOzRAZzZvLmNecDRqXy0tLy0vc3MtbyNvIzYuLjM2LTItLTExLi4tLi9pOmIucCM6YS1xIzpgLW8jbWwrYitqdDojLy5e'
url = 'https://www.iesdouyin.com/share/video/6685579095243296007/?region=CN&mid=6677477138997709575&u_code=k2a0i7cf&titleType=title&timestamp=1563358310&utm_campaign=client_share&app=aweme&utm_medium=ios&tt_from=copy&utm_source=copy'
r = requests.get(url)
with open(r'C:\\Projects\\learn\\douyin\\videos\\胡阿小小\\向暗恋的人表白的话，会发生什么?#暗恋.mp4','wb') as f:
    f.write(r.content)




# https://iu.snssdk.com/shorten/?
# version_code=6.9.1&
# pass-region=1&
# pass-route=1&
# js_sdk_version=1.17.4.3&
# app_name=aweme&
# vid=6EF6C50F-8509-457E-83B8-B2701A71CBED&
# app_version=6.9.1&
# device_id=38921967217&
# channel=App%20Store&
# mcc_mnc=46002&aid=1128&
# screen_width=750&
# openudid=347c95408a04359a962d9ef48289220c07d48310&
# os_api=18&
# ac=WIFI&
# os_version=12.1.4&
# device_platform=iphone&
# build_number=69100&
# device_type=iPhone8,1&
# iid=78133403663&
# idfa=45D6CD81-BAEB-4774-B9C0-9B5145AD4E1D&
# target=https%3A%2F%2Fwww.iesdouyin.com%2Fshare%2Fvideo%2F6685579095243296007%2F%3Fregion%3DCN%26mid%3D6677477138997709575%26u_code%3Dk2a0i7cf%26titleType%3Dtitle%26timestamp%3D1563358310%26utm_campaign%3Dclient_share%26app%3Daweme%26utm_medium%3Dios%26tt_from%3Dcopy%26utm_source%3Dcopy&
# persist=0&belong=aweme HTTP/1.1


# https://iu.snssdk.com/shorten/?build_number=69100,target=https%3A%2F%2Fwww.iesdouyin.com%2Fshare%2Fvideo%2F6685579095243296007%2F%3Fregion%3DCN%26mid%3D6677477138997709575%26u_code%3Dk2a0i7cf%26titleType%3Dtitle%26timestamp%3D1563358310%26utm_campaign%3Dclient_share%26app%3Daweme%26utm_medium%3Dios%26tt_from%3Dcopy%26utm_source%3Dcopy&persist=0&belong=aweme

