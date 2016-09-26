class Response():
	
	def __init__(self,response):
		self.response = response
		
	def get_response(self):
		return self.response
		
	def get_status_code(self):
		return self.response.status_code
		
	def get_response_header(self):
		return self.response.headers
		
	def get_response_header_keys(self):
		return self.response.headers.keys()
		
	def get_response_header_values(self):
		return self.response.headers.values()
		
	def get_response_body(self):
		return self.response.json()
		
	def get_unicoded_response_body_keys(self):
		return self.response.json().keys()
		
	def get_unicoded_response_body_values(self):
		return self.response.json().values()	
		
	def get_response_body_keys(self):
		body_keys = self.response.json().keys()
		json_keys = [key.encode('utf-8') for key in body_keys]
		return json_keys
		
	def get_response_body_values(self):
		return self.response.json().values()	
		
	def get_request_header(self):
		return self.response.request.headers	