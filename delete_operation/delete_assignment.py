import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from utils import open_asmt_list
	
def delete_grep():
	found_delete_asmt_grep()

def delete_asmt(driver, asmt_list_url, asmt_name):
	open_asmt_list(driver, asmt_list_url)
	found = found_delete_asmt(driver, asmt_name)
	while found == False:
		next_page = driver.find_element_by_css_selector("#data-table-pagination-increment-btn")
		next_page.click()
		found = found_delete_asmt(driver, asmt_name)

def found_delete_asmt(driver, asmt_name):
	rows = driver.find_elements_by_css_selector(".md-table-row")
	for row in rows:
		name = row.find_element_by_css_selector("span").text
		if asmt_name == name:
			three_point = row.find_element_by_css_selector('[aria-label="Additional Options"]')
			three_point.click()

			delete_icon = driver.find_element_by_css_selector('[aria-label = "Delete, icon"]')
			ActionChains(driver).move_to_element(delete_icon).perform()
			time.sleep(1)
			delete_icon.click()

			try:
				yes_btn = driver.find_element_by_css_selector('[aria-label="Yes"]')
				yes_btn.click()
			except NoSuchElementException, e:
				row.click()
			time.sleep(1)
			return True
	return False

def found_delete_asmt_grep(driver, grep_string):
	rows = driver.find_elements_by_css_selector(".md-table-row")
	for row in rows:
		name = row.find_element_by_css_selector("span").text
		if grep_string < name:
			three_point = row.find_element_by_css_selector('[aria-label="Additional Options"]')
			three_point.click()
			time.sleep(1)
			delete_icon = driver.find_element_by_css_selector('[aria-label = "Delete, icon"]')
			ActionChains(driver).move_to_element(delete_icon).perform()
			time.sleep(1)
			delete_icon.click()
			time.sleep(1)
			try:
				yes_btn = driver.find_element_by_css_selector('[aria-label="Yes"]')
				yes_btn.click()
				time.sleep(1)
			except NoSuchElementException, e:
				row.click()














