import requests
import logging

class Utilities(object):
	
	logger = logging.getLogger("cymon")
	
	@classmethod	
	def send_request(self,url):
		Utilities.logger.info("sending request to url: %s" %url)
		response = requests.get(url)
		Utilities.logger.info("Got the response.")
		return response
			
	@classmethod
	def get_status_code(self,response):
		Utilities.logger.info("fetching status code")
		return response.status_code
	
	@classmethod
	def get_headers(self,response):
		Utilities.logger.info("fetching headers")
		return response.headers
	
	@classmethod
	def get_json_data(self,response):
		Utilities.logger.info("Fething the response body")
		return response.json()