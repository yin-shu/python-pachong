import requests
import re
import csv

page = 0
f = open("douban.csv", mode="w")
csvwriter = csv.writer(f)

def fun(p):
  print('第' + str(p + 1) + '页')

  url = "https://movie.douban.com/top250?start=" + str(p * 25)
  headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
  }
  resp = requests.get(url, headers=headers)
  # print(resp.text)
  page_content = resp.text

  # 解析数据
  obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                  r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp;'
                  r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                  r'.*?<span>(?P<num>.*?)人评价</span>', re.S)
                  
  # 开始匹配
  result = obj.finditer(page_content)
  for it in result:
    # print(it.group('name'))
    # print(it.group('score'))
    # print(it.group('num'))
    # print(it.group('year').strip())
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())
  return

while (page < 10):
  fun(page)
  page = page + 1

f.close()
print('write over!')



