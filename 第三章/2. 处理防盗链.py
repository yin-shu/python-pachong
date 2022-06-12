# 抓取梨视频

# 1. 拿到 contId
# 2. 拿到 videoStatus 返回的 josn. -> srcURL
# 3. srcURL 里面的内容进行修整
# 4. 下载视频

import requests

url = 'https://www.pearvideo.com/video_1732555'
contId = url.split('_')[1]

videoStatusUrl = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.8938907267574385'

headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
  # 防盗链：溯源，当前本次请求的上一级是谁
  'Referer': url
}

resp = requests.get(videoStatusUrl, headers=headers)
dic = resp.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime, f'cont-{contId}')
print(srcUrl)

# 下载视频
with open('a.mp4', mode='wb') as f:
  f.write(requests.get(srcUrl).content)

