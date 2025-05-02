"""
Escribe un programa que genere la tabla de multiplicación del 1 al 10 de un número dado por el usuario.
"""

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
