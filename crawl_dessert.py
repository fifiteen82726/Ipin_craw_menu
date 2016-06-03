import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.xinshipu.com/zuofa/598664')
soup = BeautifulSoup(res.text)

title = soup.select('.re-up')
print title
