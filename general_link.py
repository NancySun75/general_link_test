import time
import random
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from bigben_login import login_bigben
from home_page import home_link
from asmt_list_add_project import local_new_project
from question_answer_project import qa_assignment
from group_project import group_assignment
from individual_project import individual_assignment
from selenium.common.exceptions import *
from bigben_driver import chrome_init, data_clear
from utils import open_asmt_list

driver = chrome_init()

login_bigben(driver)

# invoke home_link function, click link to get test moudle's link
asmt_list_url = home_link(driver, "bigbengenerallink", "bigbengenerallink: videoassignments")

open_asmt_list(driver, asmt_list_url)
local_new_project(driver, "question_answer")
qa = qa_assignment(driver, asmt_list_url)

# create a group assignment
open_asmt_list(driver, asmt_list_url)
local_new_project(driver, "group")
gp = group_assignment(driver, "Student Formed", asmt_list_url)

# create a individual assignment
open_asmt_list(driver, asmt_list_url)
local_new_project(driver, "individual")
ip = individual_assignment(driver, asmt_list_url)

data_clear(driver, asmt_list_url, [qa, gp, ip])

