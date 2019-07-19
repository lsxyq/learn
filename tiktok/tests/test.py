#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
from urllib.parse import quote

import requests

share_url = "https://reflow.huoshan.com/share/item/6701204286782721294/?tag=10392&timestamp=1563513477&watermark=2&media_type=4&&schema_url=sslocal://item?id=6701204286782721294"

share_url = str(quote(share_url))
url = "https://api.huoshan.com/hotsoon/share/link_command/?url_schema_url={}".format(share_url)
r = requests.get(url)
