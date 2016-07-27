# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup

def check_menu_page_exit(menu_url):
	try:
		res = requests.get(menu_url,timeout=1)
		return res
	except requests.exceptions.RequestException as e:    # This is the correct syntax
		return  ""

## have not confirm
def get_menu(restaurant_url):
	menu_url = restaurant_url+'/menu'
	# pass to check menu exit
	res = check_menu_page_exit(menu_url)
	if res =="":
		print "no fucking menu"
		# res = requests.get(restaurant_url+'/menu')
	else:
		soup = BeautifulSoup(res.text)
		for menu_type in soup.select(".group h2"):
			print  menu_type.text
			print "There is:"
			for detail in soup.select("table td h3"):
				print detail.contents[0].strip()

#[<a class="a37 ga_tracking" data-action="shop_15" data-category="search" data-label="店名" href="/shop/106246-大洲魚寮海鮮‧燒物" target="_blank">大洲魚寮海鮮‧燒物</a>]



# Find kind list to restaurant page
res = requests.get('http://www.ipeen.com.tw/taiwan/channel/F')
soup = BeautifulSoup(res.text)
restaurant = soup.select('.detail li a')[0].get('href')
food_kind_url = 'http://www.ipeen.com.tw'+restaurant

res = requests.get(food_kind_url)
soup = BeautifulSoup(res.text)
# print food_kind_url
# find every restaurant name and url
for restaurant in soup.select('.serShop h3'):
	if (restaurant.text.strip()[0].isdigit() == True):
		print restaurant.text.strip().replace("\t", "").replace("\n","").replace(" ","")
		print restaurant.select('a')[0].get('href')
		get_menu(restaurant.select('a')[0].get('href'))
        # requests.get('http://www.ipeen.com.tw'+restaurant.select('a')[0].get('href'))

## have not confirm
