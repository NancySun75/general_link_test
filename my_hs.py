from selenium import webdriver
import time

def home_link(driver, link, title):
	class_link = driver.find_element_by_link_text(link)
	class_link.click()

	time.sleep(10)
	
	class_title = driver.title
	if class_title == title:
		print "open successfully"
	else:
		print "failed to open"








