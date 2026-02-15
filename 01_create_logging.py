import logging
## security level 
## debug
## info
## warning
## Error
## critical
logging.basicConfig(level=logging.ERROR )

logging.log(logging.DEBUG, "LOG DEBUG message")
logging.log(logging.INFO, "LOG info message")
logging.log(logging.WARNING, "LOG Warning message")
logging.log(logging.ERROR,'This is the error message')
logging.log(logging.CRITICAL, "LOG critical message")

