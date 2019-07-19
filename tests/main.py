import requests
import re
import tkinter as tk
#用户名:<p class="name nowrap">(.*?)</p>
#简介：<p class="desc">(.*?)</p>
#封面：cover: "(.*?)"
#播放地址：playAddr: "(.*?)"
#https://aweme.snssdk.com/aweme/v1/playwm/去掉wm无水印
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
def make_it():
    #获取302重定向地址
    Text1.delete('1.0','end') #清空Text
    url = Entry1.get()
    try:
        html1 = requests.head(url)
        true_url = html1.headers['Location']
        html2 = requests.get(true_url,headers = headers)
        #print(html2.text)
        text_data = html2.text
        #视频名字
        video_name = re.findall('<p class="name nowrap">(.*?)</p>',text_data,re.S)[0]
        #视频简介
        video_summary = re.findall('<p class="desc">(.*?)</p>',text_data,re.S)[0]
        #视频封面
        #video_cover = re.findall('cover: "(.*?)"',text_data,re.S)[0]
        #视频水印播放地址
        video_player_url1 = re.findall('playAddr: "(.*?)"',text_data,re.S)[0]
        #视频去水印播放地址
        video_player_url2 = video_player_url1.replace('wm','')
        Label1_summary["text"] = video_name + '    ' + video_summary
        Text1.insert('insert',video_player_url2)
        #print(video_player_url2)
    except:
        Label1_summary["text"] = "Error"#设置标签内容
        Text1.insert('insert','Error') #Text插入文本
#以下是主函数
windows = tk.Tk()
windows.geometry('533x270')
windows.resizable(0,0)
windows.title('抖音视频无水印解析 BY：Snow')
Entry1=tk.Entry(windows)
Entry1.place(height = 36,width = 372,x = 14,y = 24)
Button1=tk.Button(windows,text = '解析',command = make_it)
Button1.place(height = 36,width = 126,x = 396,y = 24)
Label1_summary=tk.Label(windows,text = 'video简介',justify = 'left',wraplength = 508,anchor = 'n')
Label1_summary.place(height = 71,width = 508,x = 15,y = 70)
Text1=tk.Text(windows)
Text1.place(height = 108,width = 508,x = 15,y = 149)
windows.mainloop()
