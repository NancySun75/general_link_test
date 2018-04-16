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
		print "open successfully============================="
	else:
		print "failed to open================================"

	# switch window if there is new opened window
	bigben = driver.current_window_handle
	window_handles = driver.window_handles
	for handle in window_handles:
		if handle != bigben:
			driver.switch_to_window(handle)
			condition = EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Add New Item']"))
			WebDriverWait(driver, 60, 0.5).until(condition)
			asmt_list_url = driver.current_url
			print ("%s page shows===============================" %driver.title)

	return asmt_list_url


