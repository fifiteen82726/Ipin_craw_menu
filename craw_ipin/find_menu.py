import requests
import json
from bs4 import BeautifulSoup


for i in range(20000,50000):
    try:
       shop_id = i
       url =  'http://www.ipeen.com.tw/shop/' + str(i) + '/menu'
       #print shop_id
       res = requests.get(url,timeout=1)
       print i
    except requests.exceptions.RequestException as e:    # This is the correct syntax
       print e


