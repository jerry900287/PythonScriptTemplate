import os 
import sys
import time
import logging

def log_configuration_setting(log_path , log_name, log_mode, log_quantity):

	# generate log folder
	if not os.path.exists(log_path):
		os.makedirs(log_path)

	# removing old log
	file_list = []
	for file_name in os.listdir(log_path):
		if file_name.endswith(".log"):
			file_list.append(f"{log_path}\{file_name}")

	if len(file_list) >= log_quantity:
		oldest_file_name = min(file_list, key=os.path.getctime)
		os.remove(oldest_file_name)

	# set log format
	log_time = time.strftime("%Y%m%d-%H%M%S")
	log_name = f"{log_time}_{log_name}"

	if log_mode == "CRITICAL":
		log_mode = logging.CRITICAL
	elif log_mode == "ERROR":
		log_mode = logging.ERROR
	elif log_mode == "DEBUG":
		log_mode = logging.DEBUG
	elif log_mode == "INFO":
		log_mode = logging.INFO
	elif log_mode == "WARNING":
		log_mode = logging.WARNING
	elif log_mode == "NOTSET":
		log_mode = logging.NOTSET
	else:
		log_mode = None

	logging.basicConfig(level=log_mode,
				format='[%(asctime)s][%(levelname)s] %(message)s',
				datefmt='%Y-%m-%d %I:%M:%S',
				handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler(f"{log_path}\{log_name}.log", 'a+', 'utf-8')])


def main():

	logging.info(r"Testing for info")
	logging.debug(r"Testing for debug")


if __name__ == '__main__':

	# ======== [Start] Initial Setting ========

	# determine if the application is a frozen `.exe` (e.g. pyinstaller --onefile) 
	if getattr(sys, 'frozen', False):
		application_path = os.path.dirname(sys.executable)
	# or a script file (e.g. `.py` / `.pyw`)
	elif __file__:
		application_path = os.path.dirname(__file__)

	log_path = r"D:\Testing"
	#log_path = application_path
	log_name = r"Test"
	log_mode = r"INFO"
	log_quantity = 30

	log_configuration_setting(log_path, log_name, log_mode, log_quantity)
	# ======== [End] Initial Setting ========

	main()
	sys.exit(0)