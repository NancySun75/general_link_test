from selenium import webdriver
from bigben_driver import chrome_init
from login.bigben_login import login_bigben
from home_page import home_link
from asmt_list_add_project import local_new_project
from individual_project import individual_assignment

driver = chrome_init()
login_bigben(driver, "educator-1")
asmt_list_url = home_link(driver, "bigbengenerallink", "bigbengenerallink: videoassignments")
local_new_project(driver, "individual")
ip = individual_assignment(driver, asmt_list_url)
driver.quit()