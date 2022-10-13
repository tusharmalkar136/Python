
import logging

# logging.basicConfig()
# logging.critical("this is critcal msg")  50
# logging.warning("this is warning msg")
# logging.debug("this is debug msg")
# logging.error("this is error msg")
# logging.info("this is info msg")

# #
# logging.basicConfig(level=logging.CRITICAL)
# logging.critical("this is critial msg")
#
# logging.basicConfig(level=logging.ERROR)
# logging.error("this is debug msg")
#ing.basicConfig(level=logging.ERROR)
#
# logging.basicConfig(level=logging.WARNING)
# logging.warning("this is warnig")
#
# logging.basicConfig(level=20)
# logging.info('this is info')
#
# logging.basicConfig(level=10)
# logging.debug('this is debug')



logging.basicConfig(filename='logger_file.py', format='%(asctime)s' '%(message)s', filemode='w')

logger = logging.getLogger('')
# logger.setLevel(logging.WARNING)

logger.setLevel(level = 10)

logger.critical(" this is critical  msg")   # 50
logger.error("this is error msg")           # 40
logger.warning("this is warning msg")       # 30
logger.info("this is info msg")             # 20
logger.debug("this is debug msg")           # 10









