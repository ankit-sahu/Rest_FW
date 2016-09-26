
class URL(object):

	blacklist_malware = "https://cymon.io/api/nexus/v1/blacklist/ip/malware/"
	
class Codes(object):
		
	success = 200
	not_found = 404
	
class Headers(object):
	
	blacklist_malware_get = ['Allow', 'Content-Type', 'Date', 'Server', 'Vary', 'X-Frame-Options', 'transfer-encoding', 'Connection']
	blacklist_malware_head = ['Allow', 'Content-Type', 'Date', 'Server', 'Vary', 'X-Frame-Options', 'Connection']
	
class Body(object):
		
	blacklist_malware = ['count', 'previous', 'results', 'next']	
