#from cases.TestDeleteAssignment import DeleteAssignment
from cases.TestCreateAssignment import TestCreateAssignment
import unittest

suite = unittest.TestSuite()
suite.addTest(TestCreateAssignment("test_new_qa"))


runner = unittest.TextTestRunner()
runner.run(suite)