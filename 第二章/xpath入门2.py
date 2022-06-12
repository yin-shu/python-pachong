# 安装 lxml 模块
# pip3 install lxml
# xpath 解析

from lxml import etree

tree = etree.parse('a.html')
# result = tree.xpath('/html/body/ul/li/a/text()')
# result = tree.xpath('/html/body/ul/li[1]/a/text()') # xpath 的顺序是从1开始数的，【】表示索引
# result = tree.xpath('/html/body/ol/li/a[@class="daoshi"]/text()') # [@xxx=xxx] 表示属性筛选
# print(result)

ol_li_list = tree.xpath('/html/body/ol/li')
for li in ol_li_list:
  # 从每一个li中提取到文字信息
  res = li.xpath('./a/text()')  # 在li中继续去寻找，相对查找 ./
  print(res)
  res2 = li.xpath('./a/@href') # 拿到属性值： @属性
  print(res2)

print(tree.xpath('/html/body//li/a/@href'))


