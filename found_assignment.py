from selenium import webdriver


def found_asmt_by_page(driver, asmt_name):
	
	found = found_asmt(driver, asmt_name)
	while found == False:
		next_page = driver.find_element_by_css_selector("#data-table-pagination-increment-btn")
		next_page.click()
		found = found_delete_asmt(driver, asmt_name)

def found_asmt(driver, asmt_name):
	rows = driver.find_elements_by_css_selector(".md-table-row")
	for row in rows:
		name = row.find_element_by_css_selector("a").text

		if asmt_name == name:
			open_asmt(driver, row)
	return True

def open_asmt(driver, row):
	row.click()

