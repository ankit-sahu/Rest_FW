import requests
import logging

class Options(object):
	
	logger = logging.getLogger("cymon")
	
	def send_request(self,url):
		Options.logger.info("sending request to url: %s" %url)
		response = requests.get(url)
		Options.logger.info("Got the response.")
		return response
			
	def get_status_code(self,response):
		Options.logger.info("fetching status code")
		return response.status_code

	def get_headers(self,response):
		Options.logger.info("fetching headers")
		return response.headers

	def get_json_data(self,response):
		Options.logger.info("Fething the response body")
		return response.json()