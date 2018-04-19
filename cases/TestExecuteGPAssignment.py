from prepare.bigben_driver import chrome_init
from prepare.bigben_login import login_bigben
from prepare.home_page import home_link
import unittest

class TestCreateAssignment(unittest.TestCase):
	
	def setUp(self):
		self.driver = chrome_init()
		login_bigben(self.driver, "student-1")
		self.asmt_list_url = home_link(self.driver, "bigbengenerallink", "bigbengenerallink: videoassignments")

	def test_execute_gp(self):
		due_date_check()
		instructions_check()
		milestone_add()
		meeting_sechedule()
		file_add()
		video_add()
		audio_add()
		video_combine()
		mark_as_ready()
		submit_assignment()

	def tearDown(self):
		self.driver.quit()

