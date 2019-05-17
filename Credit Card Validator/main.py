credit_card_number = input("Enter the credit card number you want to validate:\n")

number_list = credit_card_number.split()

last_digit = number_list[-1]

reversed_numbers = number_list[::-1]

reversed_numbers = [int(i) for i in reversed_numbers]

i = 0

_sum = 0

for num in reversed_numbers:
    if i % 2 == 1:
        num = num*2
        if num > 9:
            num = num - 9
    i = i+1
    _sum = _sum + num

if _sum % 10 == last_digit:
    print("The number is valid")
else:
    print("Invalid credit card number")
