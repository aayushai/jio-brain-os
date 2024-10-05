import logging
import logging.handlers
import os
from logging.handlers import RotatingFileHandler

cur_dir = os.path.dirname(os.path.abspath("__file__"))
logs_data_dir = os.path.join(cur_dir, "logs/log_data")
logs_data_api_dir = os.path.join(logs_data_dir)

def get_logger(name, api_name):
	
	api_dir = os.path.join(logs_data_api_dir, api_name)
	if not os.path.isdir(api_dir):
		os.makedirs(api_dir)
	os.chmod(api_dir, 0o777)
	fname = os.path.join(api_dir, "service.log")

	f = open(fname, "w")
	f.write("")
	f.close()

	os.chmod(fname, 0o777)

	WEBAPP_CONSTANTS = {
		'LOGFILE': fname
	}

	LOGFILE = WEBAPP_CONSTANTS.get('LOGFILE', False)

	handler = RotatingFileHandler(LOGFILE, maxBytes=1048576, backupCount=5)
	
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG) 	 # MODES ERROR, INFO, DEBUG
	handler.setLevel(logging.DEBUG)  # MODES ERROR, INFO, DEBUG

	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')                           
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	
	return logger
