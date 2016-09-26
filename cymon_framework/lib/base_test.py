import unittest
import logging
import sys,os,time
from config.config import Config
from utils.cy_exception import BodyAssertionFailure
from utils.regex_parser import RegexParser

class BaseTest(unittest.TestCase):
	
	def __init__(self,*args , **kwargs):
		super(BaseTest,self).__init__(*args , **kwargs)
		
	def assertBody(self,actual,expected=None):
		body_assertions = RegexParser.evaluate(actual)
		final_assertion = None
		for value in body_assertions.values():
			if value == False:
				final_assertion = False
				break
			else:
				final_assertion = True
		self.assertTrue(final_assertion)		
		