"""
Escribe un programa que genere una escalera de asteriscos de un número dado de líneas.
"""

steps = int(input("How many steps should the staircase have?: "))

if steps < 1:
    print("Invalid input!")
    exit()  # Salir del programa

for i in range(steps + 1):
    print("*" * i)
