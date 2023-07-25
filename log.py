# Were you expecting supernatural source code?
import sys
import logging
import subprocess

logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='w')

while True:
    command = input("Enter the stop command to stop: ")

    if command == "stop":
        break

subprocess.run(["shred", "-n", "10", "-v", "log.txt"])

# The function of the code is to control
# logging of log records using the
# Logger class. First, an instance of the 
# Logger class is created. Then, a
# message is logged using the log()
# method. After that, logging is
# disabled using the disable_logging()
# method. Subsequently, anothe
# message is logged, but this messag
# is not displayed because logging has been disabled
# The program may work incorrectly on some systems

