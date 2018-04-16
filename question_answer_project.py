from selenium import webdriver
import time
import random
from selenium.common.exceptions import *
from assignment_hs import *

def qa_assignment(driver, asmt_list_url):
	name_input = asmt_name_new(driver, "_Ren_QA")
	select_due_date(driver)
	grade_types(driver, "Rubric")
	show_advanced(driver)
	instruction(driver)
	add_1st_question(driver)
	add_2nd_question(driver)
	check_all_box(driver)
	recording_option(driver)
	peer_review(driver)
	save_asmt(driver, name_input, asmt_list_url)
	return name_input	
	



