import re

class RegexParser(object):
	
	def __init__(self):
		pass
	
	@classmethod
	def evaluate(self,actual):
		
		body = {}
		count = actual["count"]
		previous = str(actual["previous"])
		next = actual["next"]
		search_results = actual["results"]
		match = re.search(r'\d', str(count))
		if match :
			body["count_res"] = True
		else:
			body["count_res"] = False
		match = re.search(r'[a-z]*',previous)
		if match :
			body["previous"] = True
		else:
			body["previous"] = False
		match = re.search(r'(http|https)://cymon.io/([\w]*[/])*[?]limit=\d*[&]offset=\d*',next)
		if match :
			body["next"] = True
		else:
			body["next"] = False
		
		test_list = []
		for each_res in search_results:
			curr_addr = each_res["addr"]
			curr_url = each_res["url"]
			match = re.search(r'^(\d{1,3}\.){3}\d{1,3}$',curr_addr)
			if match:
				test_list.append(True)
			else:
				test_list.append(False)
			match = re.search(r'(http|https)://cymon.io/(\w*[/])*(\d{1,3}\.){3}\d{1,3}$',curr_url)
			if match:
				test_list.append(True)
			else:
				test_list.append(False)	
		if False in test_list:
			body["search_results"] = False
		else:
			body["search_results"] = True
			
		return body				