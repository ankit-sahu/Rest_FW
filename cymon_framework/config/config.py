import os,sys,path
fw_root_path = os.path.abspath(os.path.dirname(os.path.join((__file__),"../../")))

class Config(object):
	
	report_path = os.path.join(fw_root_path,"report")
	log_path = os.path.join(fw_root_path,"report")
