from selenium import webdriver
from bigben_driver import chrome_init
from login.bigben_login import login_bigben
from home_page import home_link
from create_assignment.asmt_list_add_project import local_new_project
from create_assignment.question_answer_project import qa_assignment

def new_qa():
	driver = chrome_init()
	login_bigben(driver, "educator-1")
	asmt_list_url = home_link(driver, "bigbengenerallink", "bigbengenerallink: videoassignments")
	local_new_project(driver, "question_answer")
	qa = qa_assignment(driver, asmt_list_url)
	driver.quit()