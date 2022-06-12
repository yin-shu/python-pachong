# 原理： 通过第三方的一个机器去发送请求
# 上网搜索免费代理IP，比如：https://www.kuaidaili.com/free/intr/
# 14.29.139.251

import requests

proxies = {
  'https': 'https://14.29.139.251:8123'
}

resp = requests.get('https://www.baidu.com', proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)

