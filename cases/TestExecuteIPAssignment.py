from prepare.bigben_driver import chrome_init
from prepare.bigben_login import *
from prepare.home_page import home_link
from create_assignment.asmt_list_add_project import local_new_project
from create_assignment.group_project import group_assignment
from create_assignment.individual_project import individual_assignment
from execute_assignment.ExecuteIPAssignment import ExecuteIPAssignment
from execute_assignment.found_assignment import found_asmt_by_page
from delete_operation.delete_assignment import delete_asmt
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
		asmt = ExecuteIPAssignment()
		asmt.driver = self.driver
		asmt.due_date_check(self.ip, self)
		asmt.instructions_check(self.ip, self)
		'''
		
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
		logout_bigben(self.driver)
		login_bigben(self.driver, "educator-1")
		self.asmt_list_url = home_link(self.driver, "bigbengenerallink", "bigbengenerallink: videoassignments")
		delete_asmt(driver, self.asmt_list_url, self.ip["ip_name"])

		self.driver.quit()

