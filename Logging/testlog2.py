import logging

logging.basicConfig(filename="test2.log", level=logging.INFO , format='%(asctime)s %(name)s %(levelname)s %(message)s' )
try :
    logging.info("i am going to read a file")
    with open("pink.txt" , "r"):
        logging.info("successfully it has read the file")
except Exception as e:
    logging.critical("this is a situation for us")
    logging.error(e)
    logging.exception(e)
