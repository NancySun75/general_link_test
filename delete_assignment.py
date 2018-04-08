from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 

def delete_asmt(driver, asmt_name):
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
			#local delete icon and click delete to delete the assignment
			#delete_text = driver.find_elements_by_css_selector(".md-list-item .md-fake-btn")
			#time.sleep(2)
			#ActionChains(driver).move_to_element(delete_text[3]).perform()

			delete_icon = driver.find_element_by_css_selector('[aria-label = "Delete, icon"]')
			time.sleep(1)
			ActionChains(driver).move_to_element(delete_icon).perform()
			delete_icon.click()
			time.sleep(1)
			yes_btn = driver.find_element_by_css_selector('[aria-label="Yes"]')
			yes_btn.click()

			return True
	return False
# if not found, skip to next page to found.
















