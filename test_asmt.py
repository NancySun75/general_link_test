from cases.TestDeleteAssignment import DeleteAssignment
import unittest

suite = unittest.TestSuite()
suite.addTest(DeleteAssignment("test_execute_delete"))


runner = unittest.TextTestRunner()
runner.run(suite)