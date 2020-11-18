import requests

# page = requests.get('https://www.baidu.com/')
# page.encoding = 'utf-8'
# print(page.text)

page = requests.get('https://www.baidu.com/img/dong_30a61f45c8d4634ca14da8829046271f.gif')
# print(page.content)
with open('logo.gif','wb') as file:
    file.write(page.content)
