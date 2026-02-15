import logging
logging.basicConfig(level=logging.INFO)

### create the name for logger
logger = logging.getLogger("Mylogs")
gen_log_file = logging.FileHandler('D:\\Python_code\\logging\\new_log1.log')
gen_log_file.setLevel(logging.WARNING)
logger.addHandler(gen_log_file)  
print("loginpage")
logger.info("This is just information of the process")
logger.debug('This is the debug message')
logger.critical('in the critical zone')
logger.error('horrible error')
logger.warning("warn the coder")
