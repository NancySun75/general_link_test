from prepare.bigben_driver import chrome_init
from prepare.bigben_login import *
from prepare.home_page import home_link
from create_assignment.asmt_list_add_project import local_new_project
from create_assignment.group_project import group_assignment
from create_assignment.individual_project import individual_assignment
from execute_assignment.ExecuteGPAssignment import ExecuteGPAssignment
from execute_assignment.found_assignment import found_asmt_by_page
import unittest

class TestCreateAssignment(unittest.TestCase):
	
	def setUp(self):
		self.driver = chrome_init()
		login_bigben(self.driver, "educator-1")
		self.asmt_list_url = home_link(self.driver, "bigbengenerallink", "bigbengenerallink: videoassignments")
		local_new_project(self.driver, "individual")
		self.ip = individual_assignment(self.driver, self.asmt_list_url)
		logout_bigben(self.driver)
		
		login_bigben(self.driver, "student-1")
		self.asmt_list_url = home_link(self.driver, "bigbengenerallink", "bigbengenerallink: videoassignments")
		found_asmt_by_page(self.driver, self.ip["ip_name"])

	def test_execute_ip(self):
		asmt = ExecuteGPAssignment()
		asmt.driver = self.driver
		asmt.due_date_check(self.ip, self)

		'''
		instructions_check()
		milestone_add()
		meeting_sechedule()
		file_add()
		video_add()
		audio_add()
		video_combine()
		mark_as_ready()
		submit_assignment()
		'''

	def tearDown(self):
		self.driver.quit()

