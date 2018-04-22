from delete_operation.delete_assignment import delete_asmt
from prepare.bigben_driver import chrome_init
from prepare.bigben_login import *
from prepare.home_page import home_link
import unittest

class DeleteAssignment(unittest.TestCase):
	
	def setUp(self):
		self.driver = chrome_init()
		login_bigben(self.driver, "educator-1")
		self.asmt_list_url = home_link(self.driver, "bigbengenerallink", "bigbengenerallink: videoassignments")
	
	def test_execute_delete(self):
		delete_asmt_file = open('delete_operation/to_delete_asmt.txt', 'r')
		lines = delete_asmt_file.readlines()
		delete_asmt_file.close()

		for line in lines:
			name = line.replace('\n', '')
			print name
			delete_asmt(self.driver, self.asmt_list_url, name)
	
	def tearDown(self):
		self.driver.quit()
	