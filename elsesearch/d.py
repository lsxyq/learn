#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import requests

url = 'https://raw.githubusercontent.com/elastic/elasticsearch/master/docs/src/test/resources/accounts.json'
data = requests.get(url).text
with open('sales.json','w',encoding='utf8') as f:
    f.write(data)
