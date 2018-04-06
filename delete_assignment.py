from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

def delete_asmt(driver):
	found = False
	while found == False:
		rows = driver.find_elements_by_css_selector(".md-table-row")
		found = find_in_current_page(rows)
		if found == False:
			next_page = driver.find_element_by_css_selector("#data-table-pagination-increment-btn")
			next_page.click()


def find_in_current_page(rows):
	for row in rows:
		name = row.find_element_by_css_selector("span").text
		print (name, "================")
		if "04030646_Ren_QA" == name:
			three_point = row.find_element_by_css_selector('[aria-label="Additional Options"]')
			three_point.click()
			delete_li = driver.find_elements_by_css_selector("ul.md-list li")[3]
			disabled = delete_li.find_element_by_css_selector('div').get_attribute("disabled")
			if disabled == False:
				delete_li.click()
			else:
				print "This assignment is disabled to delete."
			return True
	return False