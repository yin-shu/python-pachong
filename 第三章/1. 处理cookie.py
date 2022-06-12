from requests import session

url = 'https://passport.17k.com/ck/user/login'
data = {
  'loginName': 15303232015,
  'password': 'xiao.19931201'
}
sessionObj = session() # session 可以保留上次请求的缓存，比如保留 cookie
resp = sessionObj.post(url, data)
# print(resp.text)

resp2 = sessionObj.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
print(resp2.json())