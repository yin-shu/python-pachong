# https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}
# https://dushu.baidu.com/api/pc/getChapterContent?data={%22book_id%22:%224306063500%22,%22cid%22:%224306063500|1569782244%22,%22need_bookinfo%22:1}

# 这里所谓协程，其实就是异步， 类似js 中的 async await

from email import header
from http.cookiejar import Cookie
import json
import requests
import asyncio
import aiohttp
import aiofiles

bood_id = '4306063500'
book_req_data = {
  "book_id": bood_id
}

catalog_url = f'https://dushu.baidu.com/api/pc/getCatalog?data={json.dumps(book_req_data)}'


async def aiodownload(cid, b_id, title):
  data = {
    'book_id': b_id,
    'cid': f'{b_id}|{cid}',
    'need_bookinfo': 1
  }
  data = json.dumps(data)
  url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'
  async with aiohttp.ClientSession() as session: # session 就类似 requests
    async with session.get(url) as resp:
      dic = await resp.json()
      async with aiofiles.open(f'books/{title}.txt', mode='w', encoding='utf-8') as f:
        print(dic['data'])
        await f.write(dic['data']['novel']['content'])


async def getCatalog(url):
  res = requests.get(url=url)
  list = res.json()['data']['novel']['items']
  # print(list)
  tasks = []
  for item in list:
    title = item['title']
    cid = item['cid']
    print(cid,title)
    tasks.append(aiodownload(cid, bood_id, title))

  await asyncio.wait(tasks)

if __name__ == '__main__':
  # getCatalog(catalog_url)
  asyncio.run(getCatalog(catalog_url))

