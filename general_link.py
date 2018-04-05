from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from Bongo_login import login_bongo
from my_hs import home_link
from ASMT_List_New import local_new_project
from QA_project import qa_assignment
import random
from selenium.common.exceptions import *

options = Options()
options.add_argument("user-data-dir=/tmp/tarun")
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window() # browser full screen

#cur_url = Idriver.current_url

# invoke login_bongo function to open biggen and login.
login_bongo(driver)

# invoke home_link function, click link to get test moudle's link

home_link(driver, "bigbengenerallink", "bigbengenerallink: videoassignments")
# switch window if there is new opened window
bigben = driver.current_window_handle
window_handles = driver.window_handles
for handle in window_handles:
	if handle != bigben:
		driver.switch_to_window(handle)
		print "Bongo page shows==============================="
time.sleep(20) # for waiting for new window opened completely
asmt_list_url = driver.current_url
# new a project
local_new_project(driver, "[aria-label='Create question & answer assignment']")

qa_assignment(driver, asmt_list_url)