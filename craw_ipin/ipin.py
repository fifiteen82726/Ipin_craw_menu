# get menu name 

import requests
import json
from bs4 import BeautifulSoup

#sentence.strip()
res = requests.get('http://www.ipeen.com.tw/shop/10137/menu', timeout = 0.5)
soup = BeautifulSoup(res.text)

for menu_type in soup.select(".group h2"):
    print  menu_type.text
    print "There is:"
    for detail in soup.select("table td h3"):
        print detail.contents[0].strip()

