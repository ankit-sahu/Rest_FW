import sys
import logging
import unittest
from tests.blacklist import Blacklist
# from tests.trial2 import Trial2

import time


class SuiteBuilder(object):
	
	def __init__(self):
		
		self.logger = logging.getLogger("cymon")
		# self.logger.setLevel(logging.INFO)
		
	def suite(self):
		self.logger.info("Setting up Test Suite to execute")
		testlist = [Blacklist]
		caseList = []
		for testcase in testlist:
			test_suite = unittest.TestLoader().loadTestsFromTestCase(testcase)
			caseList.append(test_suite)
		
		newsuite = unittest.TestSuite(caseList)	
		self.logger.info("New suite ready, passing suite to runner for execution..")
		return newsuite