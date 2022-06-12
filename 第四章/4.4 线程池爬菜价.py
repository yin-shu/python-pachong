# 1. 如何提取单页的数据
# 2. 上线程池，多个页面同时抓取

from operator import mod
import requests
import csv
from concurrent.futures import ThreadPoolExecutor

url = 'http://www.xinfadi.com.cn/getPriceData.html'
limit = 20

f=open('caiJia.csv', mode='w', encoding='utf-8')
csvwiter = csv.writer(f)
csvwiter.writerow(['id', 'prodName', 'prodCatid', 'prodCat', 'lowPric', 'highPric', 'avgPrice', 'place', 'unitInfo', 'pubDate'])

def download_one_page(page):
  data = {
    'limit': limit,
    'current': page
  }
  res = requests.post(url, data=data)
  list = res.json()['list']
  for i in list:
    row = [i['id'], i['prodName'], i['prodCatid'], i['prodCat'], i['lowPrice'], i['highPrice'], i['avgPrice'], i['place'], i['unitInfo'], i['pubDate']]
    csvwiter.writerow(row)

if __name__ == '__main__':
  with ThreadPoolExecutor(50) as t:
    for i in range(1, 100):
      t.submit(download_one_page, i)
      print(f'提取完毕第{i}页')

f.close()
print('下载完毕')
