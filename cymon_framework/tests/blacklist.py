from lib.base_test import BaseTest
from utils.method_factory import Method
from config.test_config import *
import logging

class Blacklist(BaseTest):

	logger = logging.getLogger("cymon")

	def test_blacklist_malware_with_get_method(self):
		Blacklist.logger.info("Satrting execution for GET header test")
		response = Method("Get").send_request(url=URL.blacklist_malware)
		self.assertEquals(response.get_status_code(),Codes.success)
		self.assertEquals(response.get_response_header_keys(),Headers.blacklist_malware_get)
		self.assertBody(response.get_response_body())
		self.assertBody(response.get_response_body())
		self.assertBody(response.get_response_body())

	def test_blacklist_malware_with_head_method():
		Blacklist.logger.info("Satrting execution for HEAD header test")
		response = Method("HEAD").send_request(url=URL.blacklist_malware)
		self.assertEquals(response.get_status_code(),Codes.success)
		self.assertEquals(response.get_response_header_keys(),Headers.blacklist_malware_head)