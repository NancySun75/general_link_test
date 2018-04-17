from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from delete_assignment import delete_asmt

def chrome_init():
	options = Options()
	options.add_argument("user-data-dir=/tmp/tarun")
	driver = webdriver.Chrome(chrome_options=options)
	driver.maximize_window() # browser full screen
	driver.implicitly_wait(60)
	return driver

def data_clear(driver, asmt_list_url, asmt_names):
	for asmt_name in asmt_names:
		delete_asmt(driver, asmt_list_url, asmt_name)
	driver.close()