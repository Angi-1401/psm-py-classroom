"""
Escribe un programa que pida un año al usuario y determine si es bisiesto.
"""

year = int(input("Enter a year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("It's a leap year!")
else:
    print("It's not a leap year.")
