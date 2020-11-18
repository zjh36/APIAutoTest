import requests
from lxml import etree

page = requests.get('http://www.biquge.info/0_383/2093437.html')
page.encoding = 'utf-8'

selector= etree.HTML(page.encoding)
selector1= selector.xpath('//div[id="content"]/text()')

for i in range(0,len(selector1)):
    with open('selector1.txt')

