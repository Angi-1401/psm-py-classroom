def is_leap(number):
    if number % 4 == 0 and (number % 100 != 0 or number % 400 == 0):
        return "It's a leap year!"
    else:
        return "It's not a leap year."


year = int(input("Enter a year: "))
print(is_leap(year))
