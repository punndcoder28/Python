import math


def e_to_nth_decimal(limit):
    some_e = round(math.e, limit)
    e_str = str(some_e)
    e_list = list(e_str)
    return some_e


decimal_limit = int(input("Enter the decimal places up to which to display E (max 15 decimals):"))
try:
    print(e_to_nth_decimal(decimal_limit))
except ValueError:
    print("Please enter a valid number")