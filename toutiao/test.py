#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import requests

cookies = {
    "odin_tt": "38dd9ab217cb45e5796fff36182f819fceb0c90497e1203d4671ec4c23f5be0abf6eba365e4e62fd7ef256c6ab122ef2",
    "tt_webid": "6637466378134963715",
    "__tea_sdk__user_unique_id": "6637466378134963715",
    "sid_guard": "c19e146271f249169156da5cd7299f6d%7C1562671427%7C5184000%7CSat%2C+07-Sep-2019+11%3A23%3A47+GMT",
    "uid_tt": "d937043025c2c481f07800dbccc2c7a7",
    "sid_tt": "c19e146271f249169156da5cd7299f6d",
    "sessionid": "c19e146271f249169156da5cd7299f6d",
    " qh[360]": "1",
    "install_id": "78133403663",
    "ttreq": "1$690cc690d51917ce9c8ba6dd76b2710178654b8d",
}
headers = {
    'accept': 'gzip, deflate',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Aweme 6.9.1 rv:69100 (iPhone; iOS 12.1.4; zh_CN) Cronet',
}
favourite_list = []
# url = 'https://aweme.snssdk.com/aweme/v1/aweme/post/?version_code=6.9.1&pass-region=1&pass-route=1&js_sdk_version=1.17.4.3&app_name=aweme&vid=6EF6C50F-8509-457E-83B8-B2701A71CBED&app_version=6.9.1&device_id=38921967217&channel=App%20Store&mcc_mnc=46002&aid=1128&screen_width=750&openudid=347c95408a04359a962d9ef48289220c07d48310&os_api=18&ac=WIFI&os_version=12.1.4&device_platform=iphone&build_number=69100&device_type=iPhone8,1&iid=78133403663&idfa=45D6CD81-BAEB-4774-B9C0-9B5145AD4E1D&min_cursor=0&user_id=94378516342&count=21&max_cursor=0'
# url = 'https://api.amemv.com/aweme/v1/aweme/post/?version_code=6.9.1&pass-region=1&pass-route=1&js_sdk_version=1.17.4.3&app_name=aweme&vid=6EF6C50F-8509-457E-83B8-B2701A71CBED&app_version=6.9.1&device_id=38921967217&channel=App%20Store&mcc_mnc=46002&aid=1128&screen_width=750&openudid=347c95408a04359a962d9ef48289220c07d48310&os_api=18&ac=WIFI&os_version=12.1.4&device_platform=iphone&build_number=69100&device_type=iPhone8,1&iid=78133403663&idfa=45D6CD81-BAEB-4774-B9C0-9B5145AD4E1D&min_cursor=0&user_id=59150254410&count=21&max_cursor=0'
url = 'https://api.amemv.com/aweme/v1/aweme/post/?version_code=6.9.1&pass-region=1&pass-route=1&js_sdk_version=1.17.4.3&app_name=aweme&vid=6EF6C50F-8509-457E-83B8-B2701A71CBED&app_version=6.9.1&device_id=38921967217&channel=App%20Store&mcc_mnc=46002&aid=1128&screen_width=750&openudid=347c95408a04359a962d9ef48289220c07d48310&os_api=18&ac=WIFI&os_version=12.1.4&device_platform=iphone&build_number=69100&device_type=iPhone8,1&iid=78133403663&idfa=45D6CD81-BAEB-4774-B9C0-9B5145AD4E1D&user_id=59150254410&max_cursor=1558747850000&count=12'
# url = 'https://aweme.snssdk.com/aweme/v1/aweme/post/?version_code=6.9.1&pass-region=1&pass-route=1&js_sdk_version=1.17.4.3&app_name=aweme&vid=6EF6C50F-8509-457E-83B8-B2701A71CBED&app_version=6.9.1&device_id=38921967217&channel=App%20Store&mcc_mnc=46002&aid=1128&screen_width=750&openudid=347c95408a04359a962d9ef48289220c07d48310&os_api=18&ac=WIFI&os_version=12.1.4&device_platform=iphone&build_number=69100&device_type=iPhone8,1&iid=78133403663&idfa=45D6CD81-BAEB-4774-B9C0-9B5145AD4E1D&min_cursor=0&user_id=58546460081&count=21&max_cursor=0'
requests.packages.urllib3.disable_warnings()

response = requests.get(url, verify=False, headers=headers, cookies=cookies)
print(response.content)

# https://www.toutiao.com/c/user/favourite/?page_type=2&user_id=55820860631&max_behot_time=0&count=20&as=

# https://www.toutiao.com/c/user/favourite/?page_type=2&user_id=55820860631&max_behot_time=0&count=20&as=A175CDF080FB785&cp=5D00DB2728D58E1&_signature=SJwMxRAdFZ5B0HbQ17Db9EicDN&max_repin_time=1559299
# https://www.toutiao.com/c/user/favourite/?page_type=2&user_id=55820860631&max_behot_time=0&count=20&as=A135DDE0705B788&cp=5D009B1718187E1&_signature=SJwMxRAdFZ5B0HbQ17Db9EicDN&max_repin_time=1557480
# https://www.toutiao.com/c/user/favourite/?page_type=2&user_id=55820860631&max_behot_time=0&count=20&as=A195CDC0A04B78A&cp=5D005BC7B87ABE1&_signature=SJwMxRAdFZ5B0HbQ17Db9EicDN&max_repin_time=155616353

# GET /login?u=454922491&verifycode=!OOZ&pt_vcode_v1=0&pt_verifysession_v1=d59898c93b7e2f034a9774ba6bf053a2be54c604add3692d1104808711ada9b801b676977cd344d09da5836c3a0a7f8154db6985b56410b0&p=bP98NRMwRhonRtH9eC*7pARlr1B5aEuiMsaDUY9zCv9GceRfAuo5RASOVswZAnmj-rTWzyGlBaVCcmdnb6XyZYvmbffVjQsI0n5JMNqkHfd0qw83mvYSF76JiHsHQrMk2gNq-79aTcf5M9iKSzJ8FmNVNDjMYp7LDDBtdSOZy5MfsrgCGP9eRxi2OToD76ciDCJZDtWsfa746w7uPx82UUhxaiaAaYcQFUuEMryemdzKVEujXgngQMAn4T54BHlJ*aysHG5Mi0LGxFF5G5BlPINNH45kM3HrSxZF5OqAnYIWk4YNxyhflwRdFjq-ZWWsHflf*KWZYQVky*G0Vq4*bw__&pt_randsalt=2&u1=https%3A%2F%2Fgraph.qq.com%2Foauth2.0%2Flogin_jump&ptredirect=0&h=1&t=1&g=1&from_ui=1&ptlang=2052&action=2-13-1562304045070&js_ver=19062020&js_type=1&login_sig=4l6R-3fTjdZ4rwQAa-OdGs-

"""
GET https://api.amemv.com/aweme/v1/aweme/post/?version_code=6.9.1&pass-region=1&pass-route=1&js_sdk_version=1.17.4.3&app_name=aweme&vid=6EF6C50F-8509-457E-83B8-B2701A71CBED&app_version=6.9.1&device_id=38921967217&channel=App%20Store&mcc_mnc=46002&aid=1128&screen_width=750&openudid=347c95408a04359a962d9ef48289220c07d48310&os_api=18&ac=WIFI&os_version=12.1.4&device_platform=iphone&build_number=69100&device_type=iPhone8,1&iid=78133403663&idfa=45D6CD81-BAEB-4774-B9C0-9B5145AD4E1D&min_cursor=0&user_id=58546460081&count=21&max_cursor=0 HTTP/1.1
Host: api.amemv.com
x-Tt-Token: 00c19e146271f249169156da5cd7299f6df0c32f784e740252dbd5110af07bb5215cf5a62704065900a6a214f78c43d81720
User-Agent: Aweme 6.9.1 rv:69100 (iPhone; iOS 12.1.4; zh_CN) Cronet
Accept-Encoding: gzip, deflate

X-Khronos: 1563269541
X-Pods: 
X-Gorgon: 8300c1cb0000b9b8abec24b362fa7c51be5823fbf7905e93c3de
"""
