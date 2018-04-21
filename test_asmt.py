from cases.TestExecuteGPAssignment import TestCreateAssignment
import unittest

suite = unittest.TestSuite()
suite.addTest(TestCreateAssignment("test_execute_ip"))


runner = unittest.TextTestRunner()
runner.run(suite)