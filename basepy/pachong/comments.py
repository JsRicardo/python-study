# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re


def getHtml(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
    
    try:
        res = requests.get(url, headers=headers, timeout=30)
        res.raise_for_status() # 状态码不是200的时候报错，进入except
        res.encoding = 'utf-8'
        return res.text
    except:
        print('请求超时')
        return ''
    
def fillBookData(commentsData, html):
    soup = BeautifulSoup(html, 'html.parser')
    commentInfo = soup.find_all('span', 'comment-info')
    
    pat = re.compile('allstar(\d+) rating')
    
    p = re.findall(pat, str(commentInfo))
    
    comments = soup.find_all('span', 'short')
    
    for i in range(1, len(comments)):
        commentsData.append( commentInfo[i - 1].a.text, comments[i].string, p[i-1] )
        
        
def printList(movieData, num):
    for i in range(num):
        u = movieData[i]
        print('''序号：{}
                    用户名：{}
                    评论内容：{}
                    评分：{}星'''.format(i+1, u[0], u[1], int(u[2]/10)))
            
def main(url):
    commentsdata = []
    
    html = getHtml(url)
    fillBookData(commentsdata, html)
    printList(commentsdata, len(commentsdata))
    
url = "https://music.douban.com/subject/35093585/"

main(url)