# Practice set-1
import logging
logging.basicConfig(filename="test.log",level=logging.INFO,filemode='w',format='%(asctime)s %(message)s')
logging.info("I am writing my new code")
logging.error("This your first error")
l = [1,2,3,4,5,6,7,8,9]
for i in l:
    if i % 2 == 0:
        logging.info(i)
        logging.info(l)
        logging.warning("This is your last warning.")
logging.shutdown()

# Practice set-2
logging.basicConfig(filename="test.log",level=logging.DEBUG,filemode='w',format='%(asctime)s %(name)s %(levelname)s %(message)s')
logging.info("subharambh")
logging.basicConfig(filename="test.log",level=logging.INFO,filemode='w',format='%(asctime)s %(name)s %(levelname)s %(message)s')
def addition(p,v):
    logging.info("we are in first step of our code.")
    try:
        logging.info("we are inside our function.")
        add = p + v
        logging.info("adding the value of %s and %s", p,v)
        return  add
    except Exception  as e:
        logging.exception(e)
print(addition(15,25))


# Practice set-3
logging.basicConfig(filename="test.log",level=logging.INFO,filemode='w',format='%(asctime)s %(time)s %(levelname)s %(message)s')
logging.info("Here we are starting our code.")
try:
    with open("test.log",'r'):
        logging.info("Successfully read the file")
except Exception as e:
    logging.error(e)
    logging.exception(e)
    logging.info("Finished")


# Practice set-4
logging.basicConfig(filename="test.log",filemode='w',format='%(asctime)s %(message)s')
# creating an object
logger = logging.getLogger()
# setting the threshold of logger to debug
logger.setLevel(logging.DEBUG)

# Test messaged
logging.info("Let's get started")
logging.debug("Harmless debug messsage")
logging.warning("HEllo World, It is warning from my side")
logging.error("It is an error")
logging.critical("Oh no! critical issue")


# importing module
import logging

# Create and configure logger
logging.basicConfig(filename="test.log",
					format='%(asctime)s %(message)s',
					filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
