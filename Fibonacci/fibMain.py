def fib_gen(limit):
    a = 1
    b = 1
    for i in range(limit):
        yield a
        a, b = b, a+b


number_limit = int(input("Enter the number of fibonacci numbers you want to see "))

for i in fib_gen(number_limit):
    print(i)