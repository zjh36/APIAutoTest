import requests
from lxml import etree

page = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
        <style>
            .item-0 {
                color: red;
            }
            .item-1 {
                color:green;
            }
        </style>
    </head>
    <body>
        <ul>
                <li class="item-0"><a href="link1.html">first item</a></li>
                <li class="item-1"><a href="link2.html">second item</a></li>
                <li class="item-inactive"><a href="link3.html">third item</a></li>
                <li class="item-1"><a href="link4.html">fouth item</a></li>
                <li class="item-0"><a href="link5.html">fifth item</a></li>
                <li class="item-0">else item</li>
        </ul>
    </body>
</html>
'''


selector = etree.HTML(page)
print(selector)

# Xpath
li = selector.xpath('//html/body/ul/li[1]/a')
print(li[0].text)

text = selector.xpath('//html/body/ul/li[2]/a/text()')
print(text)

li3 = selector.xpath('//li[@class="item-inactive"]/a')[0]
print(li3.text)

li5 = selector.xpath('//*[@href="link5.html"]')[0]
print(li5.text)

li6 = selector.xpath('//li/@class')[]


