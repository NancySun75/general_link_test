from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def home_link(driver, link, title):
	class_link = driver.find_element_by_link_text(link)
	class_link.click()
	time.sleep(5)
	class_title = driver.title
	if class_title == title:
		print "home page open successfully============================="
	else:
		print "failed to open================================"
	driver.home_handle = driver.current_window_handle
	home_handle = driver.home_handle

	asmt_list_url = switch_to_asmt(driver, home_handle)
	return asmt_list_url

	# switch window if there is new opened window
def switch_to_asmt(driver, home_handle):
	window_handles = driver.window_handles
	for handle in window_handles:
		if handle != home_handle:
			driver.switch_to_window(handle)
			condition = EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Add New Item']"))
			WebDriverWait(driver, 60, 0.5).until(condition)
			asmt_list_url = driver.current_url
			print ("%s page shows===============================" %driver.title)

	return asmt_list_url


