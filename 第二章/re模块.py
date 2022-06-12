import re

# findall： 匹配字符串中所有的符合正则的内容
list = re.findall("\d+", "我的电话号码是：10086, 身份证号是：345")

print(list)


# finditer： 匹配字符串中所有的内容【返回的是迭代器】
it = re.finditer("\d+", "我的电话号码是：10086, 身份证号是：345")
for i in it:
  print(i.group())

# search： 找到一个结果就返回， 返回的结果是 match 对象
s = re.search("\d+", "我的电话号码是：10086, 身份证号是：345")
print(s.group())


# match: 从头开始匹配
m = re.match("\d+", "10086, 身份证号是：345")
print(m.group())


# 预加载正则表达式
obj = re.compile("\d+")
ret = obj.finditer("我的电话号码是：10086, 身份证号是：345")
for it in ret:
  print(it.group())

# (?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容
s = """
<div class="aa"><span id="1">AA</span></div>
<div class="bb"><span id="2">BB</span></div>
<div class="cc"><span id="3">CC</span></div>
<div class="dd"><span id="4">DD</span></div>
<div class="ee"><span id="52">EE</span></div>
"""
obj2 = re.compile(r'<div class="(?P<class>.*?)"><span id=".*?">(?P<name>.*?)</span></div>', re.S) # re.S： 让 . 能匹配换行
res = obj2.finditer(s)
for it in res:
  print(it.group('name'), it.group('class'))

