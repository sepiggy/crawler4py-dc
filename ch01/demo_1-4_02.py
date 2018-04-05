#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree

url = 'http://www.nanrenvip8.net/find.html'


class Actress(object):
    def __init__(self, top, name, popularity, img):
        self.top = top
        self.name = name
        self.popularity = popularity
        self.img = img


def go():
    # 获得 html
    r = requests.get(url)
    r.encoding = 'utf-8'
    # xpath 解析
    s = etree.HTML(r.text)
    imgs = s.xpath('//img/@src')
    print(len(imgs))
    print(imgs)


if __name__ == '__main__':
    go()
