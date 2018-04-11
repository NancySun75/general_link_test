

# login bongo1.2 as educator-1
from selenium import webdriver
import time

def login_bigben(driver):

	home_cur_url = "https://bigben-moodle.youseeu.com"
	driver.get(home_cur_url)

	username = driver.find_element_by_id("username")
	username.clear()
	username.send_keys("educator-1") # input educator-1 as username
	password = driver.find_element_by_id("password")
	password.clear()
	password.send_keys("!QAZ2wsx")

	driver.find_element_by_css_selector('[type="submit"]').click()
# driver.find_element_by_type("submit").click()
# driver.find_element_by_class_name("btn btn-primary").click()


	