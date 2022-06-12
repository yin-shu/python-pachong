# 1. 找到未加密的参数
# 2. 想办法吧参数进行加密（必须参考网易的逻辑），params, encSecKey
# 3. 请求到网易，拿到评论信息

# 需要安装 pycrypto: pip install pycrypto
from Crypto.Cipher import AES
from base64 import b64encode
import requests
import json

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

playlist = 'A_PL_0_' # 歌单
song = 'R_SO_4_' # 歌曲

data = {
  'csrf_token': "",
  'cursor': "-1",
  'offset': "0",
  'orderType': "1",
  'pageNo': "1",
  'pageSize': "20",
  # 'rid': "A_PL_0_6883421967",
  # 'threadId': "A_PL_0_6883421967"
  'rid': "R_SO_4_1834297339",
  'threadId': "R_SO_4_1834297339"
}
e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
i = 'tB3pOtD6tKqnL9JB'

encSecKey = '851f253697187d18f9bcbca18922ec6d288c50b58e18b68896a4cf622889d25768a60013c2dde69f3182eba765875fa7274ccf776d281a1109ec207b9c7896dab7cc8ab09fa05f2c80ac430f3a847967ad5bb56e397213b33c545fb50b641bf2ecff4939ab51b0e6b3665a4b7484d5c3cc8fb7dccd0b02b47732060727d836b3'

def get_encSecKey():
  return encSecKey

def get_params(data):
  first = enc_params(data, g)
  second = enc_params(first, i)
  return second

def to_16(data):
  pad = 16 - len(data) % 16
  data += chr(pad) * pad
  return data

def enc_params(data, key): # 加密过程
  iv = '0102030405060708'
  data = to_16(data)
  aes = AES.new(key=key.encode('utf-8'), IV = iv.encode('utf-8'), mode=AES.MODE_CBC)
  bs = aes.encrypt(data.encode('utf-8'))
  return str(b64encode(bs), 'utf-8') # 转换为字符串返回


resp = requests.post(url, data = {
  'params': get_params(json.dumps(data)),
  'encSecKey': get_encSecKey()
})

dic = resp.json()
# print(dic)
hotComments = dic['data']['hotComments']
# print(hotComments)
if (hotComments != None):
  for it in hotComments:
    print(it['content'])
else:
  print('没有热评')

dd = '''
# 源码中的加密模块
function a(a) { # 生成N位随机数
    var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
    for (d = 0; a > d; d += 1)
        e = Math.random() * b.length,
        e = Math.floor(e),
        c += b.charAt(e);
    return c
}
function b(a, b) { a: 要加密的内容
    var c = CryptoJS.enc.Utf8.parse(b)
      , d = CryptoJS.enc.Utf8.parse("0102030405060708")
      , e = CryptoJS.enc.Utf8.parse(a)
      , f = CryptoJS.AES.encrypt(e, c, { # c 加密的秘钥
        iv: d, # 偏移量
        mode: CryptoJS.mode.CBC # 模式 cbc
    });
    return f.toString()
}
function c(a, b, c) {
    var d, e;
    return setMaxDigits(131),
    d = new RSAKeyPair(b,"",c),
    e = encryptedString(d, a)
}
function d(d, e, f, g) { 入口函数 d: 数据，e: 010001, f: 很长， g:xxx
    var h = {}
      , i = a(16); i: 随机数
    return h.encText = b(d, g),
    h.encText = b(h.encText, i), 返回的就是 params
    h.encSecKey = c(i, e, f),  得到的就是 encSecKey ， e 和 f 是固定的，如果把 i 固定，得到的key一定是固定的
    h
}
function e(a, b, d, e) {
    var f = {};
    return f.encText = c(a + e, b, d),
    f
}
'''
