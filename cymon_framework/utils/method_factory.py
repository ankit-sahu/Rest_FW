from get import Get
from head import Head
from options import Options

class Method(object):

	def __new__(self,method_type):
	
		method_type = method_type.lower()
			
		if method_type == "get":
			return Get()
			
		if method_type == "head":
			return Head()
			
		if method_type == "options":
			return Options()