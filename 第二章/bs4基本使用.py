# 安装
# pip3 install bs4 -i

from re import T
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.jinse.com/'
resp = requests.get(url)
# print(resp.text)

f = open('头条.csv', mode="w")
csvwriter = csv.writer(f)

# 解析数据
# 1. 把页面源代码交给 BeautifulSoup 进行处理，生成bs对象
page = BeautifulSoup(resp.text, 'html.parser') # 指定HTML解析器

# 2. 从 bs 对象中查找数据
# find(标签，属性=值)
# find_all(标签，属性=值)

# container = page.find('div', class_='js-main__l') # class 是关键字，所以需要加 _
container = page.find('div', attrs={"class": 'js-main__l'}) # 两种方式都行
# print(container)
articles = container.find_all('section', class_='js-article_item')
# print(articles)
for it in articles:
  title = it.find('span', class_="js-article_item__title--text").text.strip()
  content = it.find('p', class_="js-article_item__des").text.strip()
  author = it.find('a', class_="js-article_item__foot-author")
  views = it.find('span', class_="text")

  print(title)
  print(content)
  if (author):
    author = author.text.strip()
  else:
    author = 'null'
  if (views):
    views = views.text.strip()
  else:
    views = 'null'
  csvwriter.writerow([title, author, views, content])

f.close()
print('writer over!')