# 1. 定位到2022新片精品
# 2. 从2022新片精品中提取到子页面的链接地址
# 3. 请求子页面链接地址，拿到我们想要的下周地址

import requests
import re

domain = 'https://dy.dytt8.net/'
home = 'index2.htm'

resp = requests.get(domain + home)
resp.encoding = 'gb2312' # 指定字符集
# print(resp.text)

obj1 = re.compile(r'2022新片精品.*?<table width="100%" border="0" cellspacing="0" cellpadding="0">(?P<tb>.*?)</table>', re.S)
obj2 = re.compile(r"最新电影下载</a>]<a href='(?P<url>.*?)'>.*?《(?P<name>.*?)》", re.S)
obj3 = re.compile(r'译　　名　(?P<name1>.*?)<br />.*?片　　名　(?P<name2>.*?)<br />.*?<br /><br /><a target="_blank" href="(?P<href>.*?)"><strong>', re.S)
result1 = obj1.finditer(resp.text)

child_href_list = []
for it in result1:
  tb = it.group('tb')
  result2 = obj2.finditer(tb)
  for it2 in result2:
    url = it2.group('url')
    name = it2.group('name')
    child_href = domain + it2.group('url').strip('/')
    print(child_href, name)
    child_href_list.append(child_href)

for href in child_href_list:
  child_resp = requests.get(href)
  child_resp.encoding = 'gb2312'
  # print(child_resp.text)
  # result = obj3.finditer(child_resp.text)
  # for it in result:
  #   print(it.group('name1'), it.group('name2'), it.group('href'))
  result = obj3.search(child_resp.text)
  # print(result)
  print(result.group('name1'), result.group('name2'), result.group('href'))
