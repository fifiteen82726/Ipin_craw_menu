# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup


class Crawler(object):
	"""docstring for Crawler"""
	def __init__(self, arg):
		self.first_page_url = arg
	
	def craw_every_restaruant(self):
		# Find kind list to restaurant page
		res = requests.get(self.first_page_url)
		soup = BeautifulSoup(res.text)
		print soup.select('.detail li a')[0].get('href')

		# # 0 = 海鮮餐廳
		# restaurant = soup.select('.detail li a')[0].get('href')
		# food_kind_url = 'http://www.ipeen.com.tw'+restaurant

		# page = 1

		# for i in range(1,27):
		# 	if i == 1:
		# 		res = requests.get(food_kind_url)
		# 	else:
		# 		res = requests.get(food_kind_url+'/?p='+str(i))
		# 		print food_kind_url+'/?p='+str(i)
		# 	soup = BeautifulSoup(res.text)
		# 	# print food_kind_url
		# 	# find every restaurant name and url
		# 	for restaurant in soup.select('.serShop h3'):
		# 		if (restaurant.text.strip()[0].isdigit() == True):
		# 			print restaurant.text.strip().replace("\t", "").replace("\n","").replace(" ","")
		# 			print restaurant.select('a')[0].get('href')
		# 			#抓下menu，如果有的話
		# 			get_menu(restaurant.select('a')[0].get('href'))
		#         # requests.get('http://www.ipeen.com.tw'+restaurant.select('a')[0].get('href'))

		# ## have not confirm

craw = Crawler('http://www.ipeen.com.tw/search/taiwan/000/1-0-27-27/')
craw.craw_every_restaruant()
