import requests
import logging
from response import Response

class Head(object):
	
	logger = logging.getLogger("cymon")
	
	def send_request(self,**kwargs ):
		Head.logger.info("Sending Head request to url: %s" %kwargs["url"])
		self.response = requests.head(**kwargs)
		Head.logger.info("Got the response.")
		resp = Response(self.response)
		return resp