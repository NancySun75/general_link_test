import time
import random
from selenium.common.exceptions import *

def individual_assignment(driver, asmt_list_url):
	lt = time.localtime() #time.struct_time(tm_year=2018, tm_mon=3, tm_mday=29, tm_hour=9, tm_min=19, tm_sec=26, tm_wday=3, tm_yday=88, tm_isdst=0)
	date_str = time.strftime("%m%d%H%M", lt)
	#input Assignment name
	name_input = date_str + "_Ren_IP"
	assignment_name = driver.find_element_by_id("activity-name-textfield")
	assignment_name.send_keys(name_input)
	
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

	time.sleep(2)
	# advanced
	show_advance = driver.find_element_by_css_selector("[aria-label='Show Advanced']")
	show_advance.click()

	# input instructions
	instruction_text = driver.find_element_by_css_selector("#instructions-textfield")
	in_text_content = "This message is testing instructions text."
	instruction_text.send_keys(in_text_content)

	# input post submission instruction
	instruction_text_p = driver.find_element_by_css_selector("#post-submission-instructions-textfield")
	in_text_content_p = "This message is post submission instructions text." 
	instruction_text_p.send_keys(in_text_content_p)
	time.sleep(1)
	#Toolset default
	
	#Peer Review (allow_peer_review_before_sbmt:aprbs) (anonymous_peer_comments: apc)
	aprbs = driver.find_elements_by_css_selector("[role='checkbox'].md-fake-btn .md-text--inherit")[0]
	aprbs.click()

	show_advance = driver.find_element_by_css_selector("[aria-label='Save']")
	show_advance.click()
	time.sleep(5)
	# make sure save successfully and page skip to assignment list page.
	skip_to_url = driver.current_url
	if asmt_list_url == skip_to_url:
		print ("create individual assignment sucessfully. %s ===============================" %name_input)

	return name_input