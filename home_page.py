from selenium import webdriver
import time

def link_type(driver, link, title):
	class_link = driver.find_element_by_link_text(link)
	class_link.click()

	time.sleep(10)
	
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
			asmt_list_url = driver.current_url
			print ("%s page shows===============================" %driver.title)


	return asmt_list_url


