# find restaurant name and search link


import requests
from bs4 import BeautifulSoup


res = requests.get('http://www.ipeen.com.tw/taiwan/channel/F')
soup = BeautifulSoup(res.text)
for restaurant in soup.select('.detail li a'):
    print restaurant.text
    print restaurant.get('href')