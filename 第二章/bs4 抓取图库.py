from operator import mod
import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.bizhizu.cn/meinv/keai/'
resp = requests.get(url)
# print(resp.text)

main_page = BeautifulSoup(resp.text, 'html.parser')
con = main_page.find('div', class_='zt_list_left').find('ul')
lis = con.find_all('a')
for it in lis:
  print(it.get('href'))
  href = it.get('href')
  child_page_resp = requests.get(href)
  child_page_text = child_page_resp.text
  child_page = BeautifulSoup(child_page_text, 'html.parser')
  img_url = child_page.find('img', id='photo').get('src')
  print(img_url)
  img_resp = requests.get(img_url)
  # img_resp.content #这里拿到的是字节
  img_name = img_url.split('/')[-1] # 拿到URL中最后一个 / 以后的内容
  with open('img/' + img_name, mode='wb') as f:
    f.write(img_resp.content)
  print('over!!!', img_name)
  # time.sleep(1)
print('all over!!!!')
