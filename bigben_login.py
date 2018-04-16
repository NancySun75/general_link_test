

# login bongo1.2 as educator-1
from selenium import webdriver
import time

def login_bigben(driver, user_name):

	home_cur_url = "https://bigben-moodle.youseeu.com"
	driver.get(home_cur_url)
	user_login(driver, user_name)

def user_login(driver, user_name):
	username = driver.find_element_by_id("username")
	username.clear()
	username.send_keys(user_name) # input educator-1 as username
	password = driver.find_element_by_id("password")
	password.clear()
	password.send_keys("!QAZ2wsx")

	driver.find_element_by_css_selector('[type="submit"]').click()
	
# driver.find_element_by_type("submit").click()
# driver.find_element_by_class_name("btn btn-primary").click()
	
def logout_bigben(driver):
	switch_to_logout_window(driver)

	drop_down_list = driver.find_element_by_id("dropdown-1")
	drop_down_list.click()
	logout = driver.find_element_by_id("actionmenuaction-6")
	logout.click()
	time.sleep(3)
	print("%s shows,logout successfully============================" %driver.title) 


def switch_to_logout_window(driver):
	home_handle = driver.home_handle
	current_window = driver.current_window_handle
	all_windows = driver.window_handles

	if current_window != home_handle:
		for win in all_windows:
			if win == home_handle:
				driver.switch_to_window(win)
