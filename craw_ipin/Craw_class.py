# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re



class Crawler(object):
	"""docstring for Crawler"""
	# setUp selenium configuration
	def setUp(self):	
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = "http://www.ipeen.com.tw/"
		self.verificationErrors = []
		self.accept_next_alert = True

	def craw_every_restaruant(self):
		driver = self.driver
		driver.get(self.base_url + "/search/taiwan/000/1-0-27-27/")
		res = driver.page_source
		soup = BeautifulSoup(res)
		while len(soup.select('.next_p_one a')[0].get('href'))>0:
			for restaurant in soup.select('.serShop h3'):
				if (restaurant.text.strip()[0].isdigit() == True):
					print restaurant.text.strip().replace("\t", "").replace("\n","").replace(" ","")
					print restaurant.select('a')[0].get('href')
		# 按下一頁
			driver.find_element_by_css_selector(u"img[alt=\"下一頁\"]").click()
			res = driver.page_source
			soup = BeautifulSoup(res)
	def __init__(self, arg):
		self.first_page_url = arg
	
	def is_next_page(self, soup):
		print soup.select('.next_p_one a')[0].get('href')

	



craw = Crawler('http://www.ipeen.com.tw/search/taiwan/000/1-0-27-27/')
craw.setUp()
craw.craw_every_restaruant()
# craw.craw_every_restaruant()
