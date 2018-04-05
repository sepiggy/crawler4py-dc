#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree

url = 'https://book.douban.com/subject/1084336/comments/'
r = requests.get(url).text

s = etree.HTML(r)
print(s.xpath('//*[@id="comments"]/ul/li[8]/div[2]/p/text()'))
