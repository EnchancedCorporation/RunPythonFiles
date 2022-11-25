import sys
from colr import color
from time import sleep

class Logger:
    def __init__(self) -> None:
        pass

    def success(self, message):
        print(color("[SUCCESS]", fore='LIGHTGREEN', style='BRIGHT'), message)

    def info(self, message):
        print(color("[INFO]", fore='DARKCYAN', style='BRIGHT'), message)

    def error(self, message):
        print(color("[ERROR]", fore='RED', style='BRIGHT'), message)

logger = Logger()

try:
    file_location = sys.argv[1]
    file = open(file_location).read()
    logger.success("Found file, running in 5 seconds.")
    sleep(5)
    exec(file)
except IndexError:
    logger.info('You need to enter a file location.')
except FileNotFoundError:
    logger.error('No such file was found.')
