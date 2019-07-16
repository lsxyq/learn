#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x

#https://www.iesdouyin.com/aweme/v1/aweme/favorite/?user_id=86371592618
#&count=21&max_cursor=0&aid=1128&_signature=fBZqMxAcIH.WOSqz4s5eTHwWai&dytk=6849c66ff2a629554679fe#e4ad1343a5
#分析url https://www.iesdouyin.com/share/user/86371592618
#最终获取用户喜欢
import requests

url="https://www.iesdouyin.com/share/user/86371592618"
#抖音本身反爬虫措施
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
#获得dytk
reponse=requests.get(url,headers=headers)
reponse.encoding='utf-8'
#print(reponse.text)
#获得dytk 通过正则进行筛选
import re
dytk=re.search("dytk: '(.*?)'",reponse.text).group(1)
print(dytk)

#组装数据
params={
    'user_id':'86371592618',
    'count':'21',
    'max_cursor': '0',
    'aid': '1128',
    'dytk': dytk
}

aweme_list=[]
def get_favor_video():
    #引用全局变量
    global aweme_list
    while True:
        # 请求数据
        furl = "https://www.iesdouyin.com/aweme/v1/aweme/favorite/"
        jsonstr = requests.get(furl, params=params, headers=headers).json()
        print(jsonstr)
        # 多次请求会出现正确数据
        #修改全局变量的值
        aweme_list = jsonstr.get('aweme_list')
        print(aweme_list)
        if len(aweme_list)!=0:
            break

get_favor_video()

#进行下一步解析
#拼接视频地址
for item in aweme_list:
    #读取视频uri
    video_uri=item['video']['play_addr']['uri']
    #拼接视频地址
    video="https://aweme.snssdk.com/aweme/v1/playwm/?video_id="+video_uri
    #下载视频
    #读取视频名称
    title=item['share_info']['share_desc']
    #写入视频
    mp4=requests.get(video,headers=headers,stream=True).content
    open('F:/PythonWork/test/video/' + title+'.mp4', 'wb').write(mp4)
print("下载完成")