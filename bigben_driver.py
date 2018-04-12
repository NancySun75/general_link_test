from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def chrome_init():
	options = Options()
	options.add_argument("user-data-dir=/tmp/tarun")
	driver = webdriver.Chrome(chrome_options=options)
	driver.maximize_window() # browser full screen
	return driver