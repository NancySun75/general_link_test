from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from Bongo_login import login_bongo
from my_hs import home_link
from ASMT_List_New import local_new_project

driver = webdriver.Chrome()
#cur_url = Idriver.current_url

# invoke login_bongo function to open biggen and login.
login_bongo(driver)
# invoke home_link function, click link to get test moudle's link
home_link(driver, "bigbengenerallink", "bigbengenerallink: videoassignments")
time.sleep(10)
bigben = driver.current_window_handle
window_handles = driver.window_handles
for handle in window_handles:
	if handle != bigben:
		driver.switch_to_window(handle)
		print "Bongo page shows"
# new a project
local_new_project(driver, "[aria-label='Create question & answer project']")
