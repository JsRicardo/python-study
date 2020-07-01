# -*- coding: utf-8 -*-

import os
import requests
import urllib
import re
from PIL import Image

# 拼接每一页的网址
def getPage(keyword, page, num):
    page = page * num
    keyword = urllib.parse.quote(keyword, safe='/')
    url_str = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="
    url = url_str + keyword + "&pn=" + \
        str(page) + "&gsm=" + str(hex(page)) + \
        "&ct=&ic=0&lm=-1&width=0&height=0"

    return url

# 获取所有图片地址
def getImageUrl(pageUrl):
    try:
        res = requests.get(pageUrl, timeout=30)
        res.raise_for_status()
        html = res.text
    except Exception as e:
        print(e)
        pic_urls = []
        return pic_urls

    pic_urls = re.findall(r'"objURL":"(.*?)",', html, re.I)
    return pic_urls

# 下载图片
def downPics(keyword, pic_urls):
    for i, pic_url in enumerate(pic_urls):
        try:
            pic = requests.get(pic_url, timeout=15)
            pic.raise_for_status()
            string = keyword + '/' + str(i + 1) + '.png'
            with open(string, 'wb') as f:  # 将文件写入文件夹
                f.write(pic.content)

            img = Image.open(string)  # 打开图片，如果打开失败 报错
            print('第{}张图片下载成功，地址：{}'.format(i+1, pic_url))
            del img
        except OSError:
            print('图片不能打开')
            os.remove(string)
            continue  # 继续下载不停止
        except Exception as e:
            print('图片下载失败')
            print(e)
            continue  # 继续下载不停止


if __name__ == "__main__":
    keyword = '小清新美女'
    pagebegin = 0
    pageNum = 20
    imgNum = 2
    allPicUrls = []

    os.makedirs(keyword)
    while True:
        if pagebegin > imgNum:
            break
        url = getPage(keyword, pagebegin, pageNum)
        onePageUrl = getImageUrl(url)
        pagebegin = pagebegin+1
        allPicUrls.extend(onePageUrl)

    downPics(keyword, list(set(allPicUrls)))
