import requests
from bs4 import BeautifulSoup
from datetime import datetime
import shutil
import time
from IPython.display import Image
from random import randint

ori = requests.get("https://www.ris.gov.tw/id_card/")
soup = BeautifulSoup(ori.text)
key =  soup.select('#captchaKey')[0]["value"]

rs = requests.session()
url = "https://www.ris.gov.tw/apply/captcha/image?CAPTCHA_KEY=" + key
time =  str(int((time.time())*100)) + str(randint(0,9))
url += "&time=" + time

res = rs.get(url, headers={'referer': 'https://www.ris.gov.tw/id_card/'}, stream = True, verify =False)

f= open('check.png','wb')
shutil.copyfileobj(res.raw,f)
f.close()
Image('check.png')

