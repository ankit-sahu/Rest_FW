import requests
import logging
from response import Response

class Get(object):
	
	logger = logging.getLogger("cymon")
	
	def send_request(self,**kwargs ):
		Get.logger.info("Sending Get request to url: %s" %kwargs["url"])
		self.response = requests.get(**kwargs)
		Get.logger.info("Got the response.")
		resp = Response(self.response)
		return resp
			
	
	