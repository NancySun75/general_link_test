from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_asmt_list(driver, url):
	if driver.current_url != url:
		driver.get(url)

	condition = EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Add New Item']"))
	WebDriverWait(driver, 40, 0.5).until(condition)
	return