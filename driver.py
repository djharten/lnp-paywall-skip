import requests
import platform

from chromedriver_finder import ChromedriverFinder
from lnp import ScrapeLNP

def main():
	url = get_url()
	os_type = get_os()
	finder = ChromedriverFinder(os_type)
	driver_loc = finder.find_chromedriver()
	lnp_scraper = ScrapeLNP(url, driver_loc)
	lnp_scraper.run()

def get_url():
	url = input("Please enter the URL of the page you want to red from: ")
	return url

def get_os():
	return platform.system()

main()