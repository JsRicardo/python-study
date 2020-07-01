# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
"""
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}

r = requests.get("https://music.douban.com/subject/35093585/",headers=headers)
r.encoding = 'utf-8' # 修改编码格式

t = r.text # 整个网站的字符串

soup = BeautifulSoup(t)


comments = soup.findAll('div', 'short-content')

rege = "^[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+$"

re.match(rege, '5555@qq.com')

"""