#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# refer to https://zhuanlan.zhihu.com/p/25572729

from lxml import etree


def getxpath(html):
    return etree.HTML(html)


sample1 = """<html>
  <head>
    <title>My page</title>
  </head>
  <body>
    <h2>Welcome to my <a href="#" src="x">page</a></h2>
    <p>This is the first paragraph.</p>
    <!-- this is the end -->
  </body>
</html>
"""

s1 = getxpath(sample1)
print(s1.xpath('//title/text()'))
print(s1.xpath('/html/head/title/text()'))
print(s1.xpath('//h2/a/@src'))
print(s1.xpath('//h2/a/@href'))
print(s1.xpath('//@href'))
print(s1.xpath('//text()'))
print(s1.xpath('//comment()'))

print('-----------------------')

sample2 = """
<html>
  <body>
    <ul>
      <li>Quote 1</li>
      <li>Quote 2 with <a href="...">link</a></li>
      <li>Quote 3 with <a href="...">another link</a></li>
      <li><h2>Quote 4 title</h2> ...</li>
    </ul>
  </body>
</html>
"""

s2 = getxpath(sample2)
print(s2.xpath('//li/text()'))
# 获取第一个li
print(s2.xpath('//li[position() = 1]/text()'))
print(s2.xpath('//li[1]/text()'))
# 获取第二个li
print(s2.xpath('//li[position() = 2]/text()'))
print(s2.xpath('//li[2]/text()'))

print(s2.xpath('//li[position() mod2 = 1]/text()'))
print(s2.xpath('//li[position() mod2 = 0]/text()'))
print(s2.xpath('//li[last()]/text()'))

print(s2.xpath('//li[a]/text()'))
print(s2.xpath('//li[a or h2]/text()'))

print(s2.xpath('//a/text()|//h2/text()'))