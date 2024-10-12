import logging

logger = logging.getLogger(__name__)
#determine which log messages are actually written to the log file.
#logggin.DEBUG will capture and log messages at all levels, including DEBUG, INFO, Warning, ERROR, and CRITICAL
logger.setLevel(logging.DEBUG)

#FileHandler is an object that defines how long messages should be written to a file.
#create a file handler that will write lof messages to a file named 'test_automation.log'
handler = logging.FileHandler('./test_automation.log')
handler.setLevel(logging.DEBUG)

#Define the format for the log messages, including timestamp, logger name, log level, and the actual message
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
