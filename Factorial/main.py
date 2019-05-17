def find_factorial(n):
    if n == 0:
        return 1
    else:
        return n*find_factorial(n-1)


n = int(input("Enter the number whose factorial you want to find:"))
print("\nThe factorial of the number is:", find_factorial(n))
