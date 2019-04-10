import math


def find_prime_factors(number):
    while number%2 == 0:
        print(2)
        number = number/2

    for i in range(3, int(math.sqrt(number))+1,2):
        while number%i == 0:
            print(i)
            number = number/i

    if number>2:
        print(number)


number = int(input("Enter the number whose prime factors are to be found:"))

find_prime_factors(number)