import math


def find_next_prime(number):
   for i in range(2,number):
       if number%i == 0:
           return False, 0
       sqr = i*i
       if sqr>number:
           break
   return True, sqr


number = int(input("Enter the number whose next prime number is to be found: "))
result, next_number = find_next_prime(number)
if result:
    if next_number:
        print("Next prime number is: ")
        print(next_number)
