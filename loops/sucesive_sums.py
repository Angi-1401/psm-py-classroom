"""
Escribe un programa que pida números al usuario y vaya sumando cada entrada consecutivamente hasta que el usuario introduzca 0.
"""

num = int(input("Enter a number: "))

sum = 0

while num != 0:
    sum += num
    num = int(input("Enter a number: "))

print("The sum is:", sum)
