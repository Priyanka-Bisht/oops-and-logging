import logging
logging.basicConfig(filename="test2.log", level=logging.DEBUG , format='%(asctime)s %(name)s %(levelname)s %(message)s' )
logging.info("this is my log with timestamp")

logging.basicConfig(filename="test2.log", level=logging.INFO , format='%(asctime)s %(name)s %(levelname)s %(message)s' )
def divide(a,b):
    logging.info("the no entered by user is %s and %s", a,b)
    try:
        logging.info("we are into function")
        div = a/b
        logging.info("we have completed a division operation")
        return div
    except Exception as e:
        logging.exception(e)



(divide(5,0))


logging.basicConfig(filename="test2.log", level=logging.Error , format='%(asctime)s %(name)s %(levelname)s %(message)s' )


