import requests
from bs4 import BeautifulSoup
import os
'''
爬取网站的图片
'''

response = requests.get('https://tieba.baidu.com/f?ie=utf-8&kw=%E6%90%9E%E7%AC%91%E5%9B%BE%E7%89%87%E5%90%A7&fr=search')
soup = BeautifulSoup(response.content, 'html.parser')
imgs = soup.find_all('img')
urls = []

for img in imgs:
    src = img['src']
    bpic = img.get('bpic')
    if bpic:
        urls.append(bpic)
    if src and src.find('.jpg') != -1:
        urls.append(src)
i = 0

for url in urls:
    r_page = requests.get(url)
    with open(r'pictures' + os.sep + str(i) + '.jpg', 'wb') as p:
        p.write(r_page.content)
    i += 1
print('抓取完成')


