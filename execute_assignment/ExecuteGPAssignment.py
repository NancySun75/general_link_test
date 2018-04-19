from create_assignment.assignment_hs import *


class Execute_GP_Assignment():

	def due_date_check():
		number = get_display_number()
		set_date = get_set_date()
		now = get_current_date()
		check_during(display_number, set_date, now)

	def get_display_number():
		display_num = driver.find_element_by_css_selector('[aria-lable = "Days until due"]')
		number = int(display_num.text)
		return number 
'''
	def instructions_check():
	def milestone_add():
	def meeting_sechedule:
	def file_add():
	def video_add():
	def audio_add():
	def video_combine():
	def mark_as_ready():
	def submit_assignment:
		'''