import time
import logging
import unittest
import os,sys

fw_root = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
sys.path.append(fw_root)

from config.config import Config


logger = logging.getLogger("cymon")
file_handler = logging.FileHandler(Config.report_path + "\\cymon_{time}.log".format(time = time.time()))
formatter = logging.Formatter('%(asctime)s %(levelname)s :%(module)s:%(name)s::%(funcName)s:Line-%(lineno)s::%(message)s')
file_handler.setFormatter(formatter)
if not logger.handlers:
	logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

import HTMLTestRunner
from suite_builder import SuiteBuilder

class TestRunner(object):


	def run_test(self):
	
		test_suite = SuiteBuilder().suite()
		current_time = time.time()
		report_path = Config.report_path + "\\report_%s.html"%current_time
		outfile = open(report_path, "w")
		
		logger.info("Report path set to : %s"%report_path)
		runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report')
		logger.info("Running tests through HTMLTestRunner")
		runner.run(test_suite)
		logger.info("Exceution completed : Chek reports and log at %s"%report_path)
		
if __name__ == '__main__':
	run = TestRunner()
	run.run_test()