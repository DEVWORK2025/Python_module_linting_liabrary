def val(name):
    try:
        print("ALL are valid")
        print("No match")
    except:
        
    return "valid_name"

with open("log.log", 'w') as fo:
### reg page
    val(input(""))
    if val(input("")):
        fo.write("NAme validation succe")
    else : fo.write("Some", in_var)














import logging
import datetime as dt


def add_files():
        
    now = dt.datetime.today()

    filename = f"module_track_{now.year}-{now.month:02d}-{now.day:02d}.log"
    print(filename)

    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger("Mylogs")

    gen_log_file = logging.FileHandler(filename,)
    gen_log_file.setLevel(logging.WARNING)
    format_file = logging.Formatter("%(asctime)s : %(levelname)s --> %(message)s")

    gen_log_file.setFormatter(format_file)

    #logger.addHandler(gen_log_file)

    return logger, gen_log_file , format_file 

"""logger.info("This is just information of the process")
logger.debug('This is the debug message')
logger.critical('in the critical zone')
logger.error('horrible error')
logger.warning("warn the coder")"""

