import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ScrapeLNP:

	def __init__(self, url, chromedriver_location):
		self.url = url
		self.chromedriver_location = chromedriver_location
		self.driver = webdriver.Chrome(self.chromedriver_location)

	def run(self):
		self.__load_page()

	def __load_page(self):
		chrome_options = Options()
		chrome_options.add_experimental_option("detach", True)
		self.driver.get(self.url)
		time.sleep(600)
		self.driver.close()
