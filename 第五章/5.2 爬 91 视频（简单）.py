'''
流程：
 1. 拿到 https://91kanju.com/vod-play/54812-1-1.html 的页面源代码
 2. 从源代码中提取到 m3u8 的源代码
 3. 下载 m3u8 
 4. 读取 m3u8 文件，下载视频
 5. 合并视频
'''

import requests
import re

obj = re.compile(r"url: '(?P<url>.*?)',", re.S) # 提取 m3u8 的地址

headers = {
  # ':authority': '91kanju.com',
  ':method': 'GET',
  ':path': '/vod-play/54812-1-1.html',
  ':scheme': 'https',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'cache-control': 'max-age=0',
  'cookie': 'Hm_lvt_299b82f7848354037689582dad37e24d=1653820786; PHPSESSID=ijvo6imfnl042p1p1lf4uho3e1; Hm_lpvt_299b82f7848354037689582dad37e24d=1653821431',
  'referer': 'https://91kanju.com/vod-detail/54812.html',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}
# url = 'https://91kanju.com/vod-play/54812-1-1.html'

# resp = requests.get(url)

# # 获取 m3u8 文件
# m3u8_url = obj.search(resp.text).group('url')
# print(m3u8_url)

# # 下载 m3u8 文件
# resp2 = requests.get(m3u8_url)
# with open('哲人王后.m3u8', mode='wb') as f:
#   f.write(resp2.content)

# resp2.close()
# print('下载完毕')

# 解析 m3u8 文件
with open('哲人王后.m3u8', mode='r', encoding='utf-8') as f:
  n = 1
  for line in f:
    line = line.strip() # 先去掉空格，空白，换行符
    if line.startswith('#'): # 如果以 # 开头，抛弃
      continue
    # 下载视频片段
    resp3 = requests.get(line, headers=headers)
    f = open(f'哲人王后/{n}.ts', mode='wb')
    f.write(resp3.content)
    print(resp3.content)
    f.close()
    resp3.close()
    n+=1
