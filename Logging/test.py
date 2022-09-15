import logging
logging.basicConfig(filename="test.log" ,level = logging.INFO)
logging.info("this is my very first code for logging")
logging.warning("this is warning from my side")
l = [1,2,3,465,6,5]
for i in l:
    if i == 2:
        logging.info(i)
        logging.info(l)
        logging.warning("this is a warning for a user that they have found out 2 in list")

logging.shutdown()

# There are five types of logging level:
# 1)info-20 2)debug-10 3)warning-30 4)error-40 5)critical-50

