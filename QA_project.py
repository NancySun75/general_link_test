from selenium import webdriver
import time
import random
from selenium.common.exceptions import *

def qa_assignment(driver, asmt_list_url):
	lt = time.localtime() #time.struct_time(tm_year=2018, tm_mon=3, tm_mday=29, tm_hour=9, tm_min=19, tm_sec=26, tm_wday=3, tm_yday=88, tm_isdst=0)
	date_str = time.strftime("%m%d%H%M", lt)
	#input Assignment name
	name_input = date_str + "_Ren_QA"
	assignment_name = driver.find_element_by_id("activity-name-textfield")
	assignment_name.send_keys(name_input)
	
	#select due date and due time
	
	due_date = driver.find_element_by_id("due-date-datepicker")
	due_date.click()
	# make sure date by calander

	day_str = time.strftime("%d", lt)
	day_num = int(day_str)
	print ("date select the", day_num, "===============================gggggg")
	time.sleep(2)
	day_args = driver.find_elements_by_css_selector("button.md-calendar-date")
	day_args[day_num].click()
	ok_btn = driver.find_elements_by_css_selector("button.md-ink--primary")[1]
	ok_btn.click()
	# not support input date
	'''
	date_input = time.strftime("%m/%d%Y", lt)
	due_date.send_keys(date_input)
	'''
	
	
	
	'''
	due_time = driver.find_element_by_id("due-time-timepicker") # or: _css_selector("#due-date-timepicker")
	due_time.click()
	date_select_time = driver.find_element_by_css_selector()
	'''
	
	time.sleep(2)
	
	# advanced
	show_advance = driver.find_element_by_css_selector("[aria-label='Show Advanced']")
	show_advance.click()

	# input instructions
	instruction_text = driver.find_element_by_css_selector("#instructions-textfield")
	in_text_content = "This message is testing instructions text. It requests not more than 400 charactors and allow to input kinds of specific charactors. So I need test ""~!@#$%^&*()_+{}:|>?`1234567890-=[];'\,./ at the same time. This will contain 2 check points about instruction text.above is 263 charactors, I need more charactors to fill. so below is test message test message test message test message test message 400"
	instruction_text.send_keys(in_text_content)

	# input post submission instruction
	instruction_text_p = driver.find_element_by_css_selector("#post-submission-instructions-textfield")
	in_text_content_p = "This message is post submission instructions text." 
	instruction_text_p.send_keys(in_text_content_p)

	# Questions
	add_question = driver.find_element_by_css_selector("[aria-label='Add Question']")
	add_question.click()
	question_text1 = driver.find_element_by_css_selector('#question-text0')
	the_1st_question = "This is the first question test."
	question_text1.send_keys(the_1st_question)
	# add the second question
	add_question.click()
	question_text2 = driver.find_element_by_css_selector('#question-text1')
	the_2nd_question = "This is the second question test."
	question_text2.send_keys(the_2nd_question)

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
	num_of_RR = random.randint(0, 999)
	peer_review_amount = driver.find_element_by_css_selector("#peer_review_amount")
	peer_review_amount.clear()
	peer_review_amount.send_keys(num_of_RR)
	time.sleep(3)

	show_advance = driver.find_element_by_css_selector("[aria-label='Save']")
	show_advance.click()
	time.sleep(5)
	# make sure save successfully and page skip to assignment list page.
	skip_to_url = driver.current_url
	if asmt_list_url == skip_to_url:
		print ("create QA assignment sucessfully. %s ===============================" %name_input)











