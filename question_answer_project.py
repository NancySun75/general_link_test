from selenium import webdriver
import time
import random
from selenium.common.exceptions import *
from assignment_hs import *

def qa_assignment(driver, asmt_list_url):
	asmt_name_new(driver, "_Ren_QA")
	grade_types(driver, "Five Star")
	select_due_date(driver)
	show_advanced(driver)
	instruction(driver)
	add_1st_question(driver)
	add_2nd_question(driver)

	# Recording Options: default
	checkbox_divs = driver.find_elements_by_tag_name("div")
	# filter out all elements whose type is checkbox
	for i in checkbox_divs:
		try: # this exception setting is for checked "Random Qestion Mode" will add an option: number of randmom qestions per student
			if i.get_attribute('role') == 'checkbox' and i.get_attribute('aria-checked') == "false":
				i.click()		
		except StaleElementReferenceException:
				print "This exception cause by no Delay options when checking Record Reaction."
	time.sleep(3)
	# need to input amount of random questions if select Random question mode
	random_qestion_num = driver.find_element_by_css_selector("#amount_of_random_questions")
	random_qestion_num.send_keys(random.randint(1,2))
	# Peer Review
	# generate a random for "Number of Required Reviews"
	# remember import random
	num_of_RR = random.randint(0, 3)
	peer_review_amount = driver.find_element_by_css_selector("#peer_review_amount")
	peer_review_amount.clear()
	peer_review_amount.send_keys(num_of_RR)
	time.sleep(3)

	show_advance = driver.find_element_by_css_selector("[aria-label='Save']")
	show_advance.click()
	time.sleep(5)
	# make sure save successfully and page skip to assignment list page.
	asmt_list_page = driver.current_url
	if asmt_list_url == asmt_list_page:
		print ("create QA assignment sucessfully. %s ===============================" %name_input)

	



