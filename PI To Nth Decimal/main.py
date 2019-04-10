import math


def pi_to_nth_decimal(limit):
    # rounding off the pi value to the limit
    some_pi = round(math.pi, limit)
    # convert it into string to hold larger decimal places
    pi = str(some_pi)
    # convert the string to list
    pi_list = list(pi)
    return some_pi


roundTo = int(input("Enter the number of decimal places in pi to be displayed (max of 15 decimal places will be "
                    "displayed): "))

try:
    print(pi_to_nth_decimal(roundTo))
except ValueError: # ValueError to check if the input entered is not a number
    print("Enter a valid number")
