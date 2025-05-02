"""
Escribe un programa que pida al usuario 10 números y devuelva una lista excluyendo todos los duplicados ingresados.
"""

numbers = []

for i in range(10):
    number = int(input("Enter a number (" + str(i + 1) + "/10): "))
    if number not in numbers:
        numbers.append(number)


print("List of unique numbers:", numbers)
