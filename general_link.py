from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from bigben_login import login_bigben
from home_page import home_link
from asmt_list_add_project import local_new_project
from question_answer_project import qa_assignment
from group_project import group_assignment
from individual_project import individual_assignment
import random
from selenium.common.exceptions import *
from delete_assignment import delete_asmt

options = Options()
options.add_argument("user-data-dir=/tmp/tarun")
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window() # browser full screen

# invoke login_bigben function to open biggen and login.
login_bigben(driver)

# invoke home_link function, click link to get test moudle's link
asmt_list_url = home_link(driver, "bigbengenerallink", "bigbengenerallink: videoassignments")
condition = EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Add New Item']"))


'''
# new a project
# create a QA assignment
WebDriverWait(driver, 20, 0.5).until(condition)
local_new_project(driver, "question_answer")
qa = qa_assignment(driver, asmt_list_url, "Five Star")

# create a group assignment
WebDriverWait(driver, 20, 0.5).until(condition)
local_new_project(driver, "group")
gp = group_assignment(driver, "Student Formed", asmt_list_url)

# create a individual assignment
WebDriverWait(driver, 20, 0.5).until(condition)
local_new_project(driver, "individual")
ip = individual_assignment(driver, asmt_list_url)
'''
WebDriverWait(driver, 20, 0.5).until(condition)
local_new_project(driver, "question_answer")
qa2 = qa_assignment(driver, asmt_list_url)
'''
#delete created assignment
WebDriverWait(driver, 20, 0.5).until(condition)
delete_asmt(driver, qa2)
'''