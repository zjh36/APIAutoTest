import requests
from lxml import etree

page = requests.get('http://www.biquge.info/0_383/1596644.html')
page.encoding = 'utf-8'


prone1= etree.HTML(page.content)
prone3= prone1.xpath('//h1')
prone2 = prone1.xpath('//div[@id="content"]/text()')


for i in range(0,len(prone3)):
    with open('novel.txt','a',encoding='utf-8') as file:
        file.write(str(prone3[i])+'\n')
        
for i in range(0,len(prone2)):
    with open('novel.txt','a',encoding='utf-8') as file:
        file.write(str(prone2[i])+'\n')

print(prone2)