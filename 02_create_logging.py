import logging

logging.basicConfig(level=logging.INFO)
### create the name for logger
logger = logging.getLogger("Mylogs")
logger.info("This is just information of the process")
logger.critical("jjk")

logger1 = logging.getLogger("Currlogs")
logger1.error("Error in curr")