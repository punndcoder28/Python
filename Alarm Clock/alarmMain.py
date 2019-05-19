
"""
    This is a simple command line based alarm where you pass in the number of the
    after which the alarm wakes up through the terminal after the python3 alarmMain.py
    command
"""

import sys
from time import sleep

command_line_arg = sys.argv
length = len(command_line_arg)

if length != 2:
    print("Enter the duration (in minutes) after the python3 alarmMain.py command")
    print("Enter 0 to test the script immediately")
    exit(0)

try:
    duration = int(command_line_arg[1])
except ValueError:
    print("Please enter a valid duration of more than or equal to 0")
    exit(0)

if duration < 0:
    print("Enter a value more than or equal to 0")
    exit(0)

seconds = duration * 60

if duration == 1:
    units = 'minute'
else:
    units = 'minutes'

try:
    if duration > 0:
        print("Sleeping for "+str(duration)+" "+units)
        sleep(seconds)
    print("WAKE UP!!!!")
    for i in range(10):
        print(chr(7))
        sleep(0.5)
except KeyboardInterrupt:
    print("\nInterrupted!!")
    exit(0)
