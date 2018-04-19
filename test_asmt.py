
from cases.TestCreateAssignment import TestCreateAssignment
import unittest

suite = unittest.TestSuite()
suite.addTest(TestCreateAssignment("test_new_qa"))
suite.addTest(TestCreateAssignment("test_new_gp"))
suite.addTest(TestCreateAssignment("test_new_ip"))

runner = unittest.TextTestRunner()
runner.run(suite)