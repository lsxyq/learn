#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
from bs4 import BeautifulSoup as bs
import requests


def download_html(url):
    response = requests.get(url, )
    html = response.content.decode('utf8')
    with open('a.html','w',encoding='utf8') as f:
        f.write(html)
    parser_html(html)


def parser_html(html):
    bs_intance = bs(html)
    print(bs_intance.text)


url ='https://tiku.dev.yiqizuoti.com/v4-index-29859991.html#/v4/question'
download_html(url)