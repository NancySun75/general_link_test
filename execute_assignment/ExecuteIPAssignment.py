from create_assignment.assignment_hs import *
from datetime import datetime 

class ExecuteIPAssignment():

	def due_date_check(self, ip, test_case):
		set_date = self.get_set_date()
		asmt_date = self.get_asmt_date(ip)
		test_case.assertIn(asmt_date, set_date, msg = "Due date is not equal to created due date.")
		
		display_number = self.get_display_number()
		now = datetime.now()
		set_date_value = datetime.strptime(set_date, "%m/%d/%Y, %H:%M %p")
		delta_value = (set_date_value - now).days
		test_case.assertEqual(display_number, delta_value, msg = "delta_value is unconsistent with display_number")

	def get_display_number(self):
		display_num = self.driver.find_element_by_css_selector('[aria-label = "Days until due"]')
		display_number = int(display_num.text)
		return display_number

	def get_set_date(self):
		due_date = self.driver.find_element_by_css_selector('[aria-label = "Due Date"]')
		set_date = due_date.text
		return set_date

	def get_asmt_date(self, ip):
		return ip["due_date"]

	def instructions_check(self, ip, test_case):
		ins_title = self.driver.find_element_by_css_selector(".instructions-title .md-card-title--title")
		instructions_title = ins_title.text
		test_case.assertEqual(instructions_title, "Instructions", msg = "instructions-title is wrong")

		ins_text = self.driver.find_element_by_css_selector(".instructions-detail-container")
		instructions_text = ins_text.text
		input_ins_text = ip["ins"]["ins_text"]
		test_case.assertEqual(instructions_text, input_ins_text, msg = "instructions content is unconsistent")
'''

	def milestone_add():
	def meeting_sechedule:
	def file_add():
	def video_add():
	def audio_add():
	def video_combine():
	def mark_as_ready():
	def submit_assignment:
'''