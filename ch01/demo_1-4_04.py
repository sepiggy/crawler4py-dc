#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lxml import etree

import requests

url = 'https://book.douban.com/subject/1084336/comments/'


def get_request(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r


def get_xpath(request):
    html = etree.HTML(request.text)
    return html


def get_comments(html):
    comments = html.xpath('//*[@id=“comments”]/ul/li/div[2]/p/text()')
    return comments


def go():
    request = get_request(url)
    html = get_xpath(request)
    comments = get_comments(html)
    print(comments)


if __name__ == '__main__':
    go()
