# 安装 lxml 模块
# pip3 install lxml
# xpath 解析

from lxml import etree

xml = """
<book>
  <id>1</id>
  <name>床前明月光</name>
  <price>1.22</price>
  <nick>疑是地上霜</nick>
  <author>
    <nick id="10086">疑是地上霜</nick>
    <nick id="100861">孙悟空</nick>
    <nick id="100862">猪八戒</nick>
    <nick id="100863">唐三藏</nick>
    <nick id="100864">沙和尚</nick>
    <div>
      <nick>白龙马</nick>
    </div>
    <span>
      <nick>白龙马2</nick>
    </span>
  </author>
  <partner>
    <nick>东伯雪鹰</nick>
  </partner>
</book>
"""

tree = etree.XML(xml)
# result = tree.xpath('/book') # / 表示层级关系，第一个/ 是根节点
# result = tree.xpath('/book/name') 
# result = tree.xpath('/book/name/text()') # text() 拿文本
# result = tree.xpath('/book/author//nick/text()') # // 表示在所有后代中查找
result = tree.xpath('/book/author/*/nick/text()') #  * 任意节点
print(result)

