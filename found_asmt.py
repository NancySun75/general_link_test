


def found_asmt(driver, asmt_name):
	rows = driver.find_elements_by_css_selector(".md-table-row")
	for row in rows:
		name = row.find_element_by_css_selector("span").text

		if asmt_name == name:
			three_point = row.find_element_by_css_selector('[aria-label="Additional Options"]')
			three_point.click()