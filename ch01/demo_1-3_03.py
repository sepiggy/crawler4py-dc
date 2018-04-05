# -*- coding:utf-8 -*-

# 爬取网页的通用框架:
## 定义函数
## 设置超时
## 异常处理
## 调用函数

import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(getHTMLText(url))
