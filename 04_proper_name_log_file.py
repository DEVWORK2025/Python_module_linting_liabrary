import logging
import datetime as dt

now = dt.datetime.today()

## filename = f"tracker_{}-{}-{}.log"
## filename = f"tracker_{now.year}-{now.month}-{now.day}.log"
filename = f"tracker_{now.year}-{now.month:02d}-{now.day:02d}.log"
print(filename)

logging.basicConfig(level=logging.INFO)

### create the name for logger

logger = logging.getLogger("Mylogs")

gen_log_file = logging.FileHandler(filename)
gen_log_file.setLevel(logging.WARNING)

logger.addHandler(gen_log_file)  

logger.info("This is just information of the process")
logger.debug('This is the debug message')
logger.critical('in the critical zone')
logger.error('horrible error')
logger.warning("warn the coder")

