import requests
from bs4 import BeautifulSoup

response = requests.get('https://tieba.baidu.com/f?ie=utf-8&kw=%E6%90%9E%E7%AC%91%E5%9B%BE%E7%89%87%E5%90%A7&fr=search')
soup = BeautifulSoup(response.content, 'html.parser')
img = soup.find_all('img')
print(img)