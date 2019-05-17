# This is a simple terminal based unit converter that can be used to convert from one
# system to another.

# things to do:
# TEMPERATURE CONVERSIONS
# 1. Convert from celcius to fahrenheit
# 2. Convert from fahrenheit to celcius
# METRIC CONVERSIONS
# 3. Convert from cm to in
# 4. Convert from in to cm
# 5. Convert from ft to in
# 6. Convert from ft to m
# Mass Conversions
# 7. Kilo to pound
# 8. Pound to Kilo
# 9. Kilo to ounce
# 10. Ounce to kilo


def f_to_c(temp_f):
    return (temp_f-32)*(5/9)


def c_to_f(temp_c):
    return temp_c*(9/5)+32


def cm_to_in(unit_cm):
    return unit_cm/2.54


def in_to_cm(unit_in):
    return unit_in*2.54


def ft_to_in(unit_ft):
    return unit_ft*12


def in_to_ft(unit_in):
    return unit_in/12


def ft_to_m(unit_ft):
    return unit_ft/3.281


def m_to_ft(unit_m):
    return unit_m*3.281


def kg_to_pound(unit_kg):
    return unit_kg*2.20462


def pound_to_kg(unit_pound):
    return unit_pound/2.20462


def kilo_to_ounce(unit_kg):
    return unit_kg*35.247


def ounce_to_kilo(unit_ounce):
    return unit_ounce/35.247


print("Welcome to the Unit conversion Program")
print("Choose the type of conversion you would like: ")
ch = int(input("1.Temperature conversion \n2.Metric conversion\n3.Mass conversion\n"))
if ch == 1:
    ch1 = int(input("1.Fahrenheit to Celcius\n2.Celcius to Fahrenheit\n"))
    if ch1 == 1:
        ch2 = int(input("Enter the temperature in fahrenheit:"))
        print(f_to_c(ch2))
    else:
        ch2 = int(input('Enter the temperature in celcius:'))
        print(c_to_f(ch2))
elif ch == 2:
    ch1 = int(input("1.cm to in\n2.in to cm\n3.ft to in\n4.ft to m\n5.in to ft\n6.m to ft"))
    if ch1 == 1:
        ch2 = int(input("Enter length in cm:"))
        print(cm_to_in(ch2))
    elif ch1 == 2:
        ch2 = int(input("Enter length in inches:"))
        print(in_to_cm(ch2))
    elif ch1 == 3:
        ch2 = int(input("Enter length in feet:"))
        print(ft_to_in(ch2))
    elif ch1 == 4:
        ch2 = int(input("Enter length in feet:"))
        print("The approximate value is:")
        print(ft_to_m(ch2))
    elif ch1 == 5:
        ch2 = int(input("Enter length in inches:"))
        print(in_to_ft(ch2))
    else:
        ch2 = int(input("Enter length in meter:"))
        print("The approximate value is:")
        print(m_to_ft(ch2))
else:
    ch1 = int(input("\n1.Kilo to pound\n2.Pound to kilo\n3.Kilo to ounce\n4.Ounce to kilo"))
    if ch1 == 1:
        ch2 = int(input("Enter the weight in kilo:"))
        print(kg_to_pound(ch2))
    elif ch1 == 2:
        ch2 = int(input("Enter weight in pounds:"))
        print(pound_to_kg(ch2))
    elif ch1 == 3:
        ch2 = int(input("Enter the weight in kilo:"))
        print(kilo_to_ounce(ch2))
    elif ch1 == 4:
        ch2 = int(input("Enter the weight in ounces:"))
        print(ounce_to_kilo(ch2))
