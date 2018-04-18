from selenium import webdriver
import time
import random
from selenium.common.exceptions import *

lt = time.localtime() #time.struct_time(tm_year=2018, tm_mon=3, tm_mday=29, tm_hour=9, tm_min=19, tm_sec=26, tm_wday=3, tm_yday=88, tm_isdst=0)
date_str = time.strftime("%m%d%H%M", lt)

def asmt_name_new(driver, custumer_patern):	
	#input Assignment name
	name_input = date_str + custumer_patern
	assignment_name = driver.find_element_by_id("activity-name-textfield")
	assignment_name.send_keys(name_input)
	return name_input

#select the grade type
def grade_types(driver, grade_type):
	grade_type_toggle = driver.find_element_by_id("grade-type-toggle")
	grade_type_toggle.click()
	grade_type_dics = {
		"Percentage":"[data-id = '0']",
		"Rubric":"[data-id = '1']",
		"Pass/Fail":"[data-id = '2']",
		"Auto Pass":"[data-id = '3']",
		"Five Star":"[data-id = '4']",
	}
	grade_type_select = driver.find_element_by_css_selector(grade_type_dics[grade_type])
	grade_type_select.click()
	if grade_type == "Rubric":
		rubric(driver, "examplerubric.csv")

# select rubric
def rubric(driver, rubric_name):
	time.sleep(1)
	rubric_toggle = driver.find_element_by_css_selector('[aria-label="Rubric"]')
	#rubric_toggle.clear() # setting for edit, use it when editing
	rubric_toggle.click()

	rubric_list_items = driver.find_elements_by_css_selector(
		"#rubric-menu-options .md-list-item .md-tile-content")
	for i in rubric_list_items:
		if rubric_name == i.text:
			i.click()
			break

def select_due_date(driver):
	#select due date and due time
	due_date = driver.find_element_by_id("due-date-datepicker")
	due_date.click()
	# make sure date by calander
	day_str = time.strftime("%d", lt)
	day_num = int(day_str)
	print ("date select the", day_num, "===============================")
	time.sleep(2)
	day_args = driver.find_elements_by_css_selector("button.md-calendar-date")
	day_args[day_num].click()
	ok_btn = driver.find_elements_by_css_selector("button.md-ink--primary")[1]
	ok_btn.click()
	time.sleep(1)
	'''
	due_time = driver.find_element_by_id("due-time-timepicker") # or: _css_selector("#due-date-timepicker")
	due_time.click()
	date_select_time = driver.find_element_by_css_selector()
	'''

def show_advanced(driver):
	# advanced
	show_advance = driver.find_element_by_css_selector("[aria-label='Show Advanced']")
	show_advance.click()

def instruction(driver):
	# input instructions
	instruction_text = driver.find_element_by_css_selector("#instructions-textfield")
#	in_text_content = "This message is testing instructions text. It requests not more than 400 charactors and allow to input kinds of specific charactors. So I need test ""~!@#$%^&*()_+{}:|>?`1234567890-=[];'\,./ at the same time. This will contain 2 check points about instruction text.above is 263 charactors, I need more charactors to fill. so below is test message test message test message test message test message 400"
	in_text_content = "This message is testing instructions text."
	instruction_text.send_keys(in_text_content)

	# input post submission instruction
	instruction_text_p = driver.find_element_by_css_selector("#post-submission-instructions-textfield")
	in_text_content_p = "This message is post submission instructions text." 
	instruction_text_p.send_keys(in_text_content_p)

	# Questions
	# add the first question
def add_1st_question(driver):
	add_question = driver.find_element_by_css_selector("[aria-label='Add Question']")
	add_question.click()
	question_text1 = driver.find_element_by_css_selector('#question-text0')
	the_1st_question = "This is the first question test."
	question_text1.send_keys(the_1st_question)

	# add the second question
def add_2nd_question(driver):
	add_question = driver.find_element_by_css_selector("[aria-label='Add Question']")
	add_question.click()
	question_text2 = driver.find_element_by_css_selector('#question-text1')
	the_2nd_question = "This is the second question test."
	question_text2.send_keys(the_2nd_question)

def check_all_box(driver):
	# Recording Options: default
	checkbox_divs = driver.find_elements_by_tag_name("div")
	# filter out all elements whose type is checkbox
	for i in checkbox_divs:
		try: # this exception setting is for checked "Random Qestion Mode" will add an option: number of randmom qestions per student
			if i.get_attribute('role') == 'checkbox' and i.get_attribute('aria-checked') == "false":
				i.click()		
		except StaleElementReferenceException:
				print "This exception cause by no Delay options when checking Record Reaction."
	time.sleep(1)

# need to input amount of random questions if select Random question mode
def recording_option(driver):
	random_qestion_num = driver.find_element_by_css_selector("#amount_of_random_questions")
	random_qestion_num.send_keys(random.randint(1,2))

# for group_assignment 	
def group_formeds(driver, group_formed):
	if group_formed != "Educator Formed":
		group_formation = driver.find_element_by_id("executors_type-toggle")
		group_formation.click()
		time.sleep(1)
		student_formed = driver.find_element_by_css_selector("[data-id='1']")
		system_formed = driver.find_element_by_css_selector("[data-id='2']")
		
		if group_formed == student_formed.find_element_by_css_selector("div").text:
			student_formed.click()
		else:
			system_formed.click()
		time.sleep(1)
		#Finalize groups at date/time: current_time + after 10mins
		finalize_date = driver.find_element_by_id("finalize-group-date-datepicker")
		finalize_date.click()
		time.sleep(1)
		ok_btn1 = driver.find_elements_by_css_selector(".md-ink--primary")[1]
		ok_btn1.click()
		time.sleep(1)
		finalize_time = driver.find_element_by_id("finalize-group-date-timepicker")
		finalize_time.click()
		time.sleep(1)
		ok_btn2 = driver.find_elements_by_css_selector(".md-ink--primary")[1]
		ok_btn2.click()
		time.sleep(1)
		#Minimum students per group: default 1
		#Maximum students per group:
		max_stn = driver.find_element_by_id("max_students_amount")
		max_stn.clear()
		max_stn.send_keys(3)
		time.sleep(1)

#Peer Review (allow_peer_review_before_sbmt:aprbs) (anonymous_peer_comments: apc)		
def peer_review(driver):
	num_of_RR = random.randint(0, 3)
	peer_review_amount = driver.find_element_by_css_selector("#peer_review_amount")
	peer_review_amount.clear()
	peer_review_amount.send_keys(num_of_RR)
	time.sleep(3)

def save_asmt(driver, name_input, asmt_list_url):
	show_advance = driver.find_element_by_css_selector("[aria-label='Save']")
	show_advance.click()
	time.sleep(5)
	# make sure save successfully and page skip to assignment list page.
	asmt_list_page = driver.current_url
	if asmt_list_url == asmt_list_page:
		print ("create assignment sucessfully. %s ===============================" %name_input)
