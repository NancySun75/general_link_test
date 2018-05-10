from prepare.bigben_driver import chrome_init
from prepare.bigben_login import login_bigben
from prepare.home_page import home_link
from create_assignment.asmt_list_add_project import local_new_project
from create_assignment.question_answer_project import qa_assignment
from create_assignment.individual_project import individual_assignment
from create_assignment.group_project import group_assignment
import unittest

class TestCreateAssignment(unittest.TestCase):
	
	def setUp(self):
		self.driver = chrome_init()
		login_bigben(self.driver, "educator-1")
		#self.asmt_list_url = home_link(self.driver, "bigbengenerallink", "bigbengenerallink: videoassignments")
		self.asmt_list_url = home_link(self.driver, "13StableGeneralCourse", "13stablegen: 13StableGeneralVideoAssignments")

	def test_new_qa(self):
		local_new_project(self.driver, "question_answer")
		qa = qa_assignment(self.driver, self.asmt_list_url)
	"""	
	def test_new_gp(self):
		local_new_project(self.driver, "group")
		gp = group_assignment(self.driver, self.asmt_list_url)

	def test_new_ip(self):
		local_new_project(self.driver, "individual")
		ip = individual_assignment(self.driver, self.asmt_list_url)
	"""
	def tearDown(self):
		self.driver.quit()

