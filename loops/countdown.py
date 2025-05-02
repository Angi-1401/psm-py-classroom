"""
Escribe un programa que pida al usuario un número y calcule la cuenta regresiva hacia 0 por cada segundo trasncurrido en tiempo real.
"""

import time  # Librería para emplear el tiempo real del sistema

num = int(input("Enter a number: "))

if num <= 0:
    print("Invalid input!")
    exit()  # Salir del programa

while num > 0:
    print(num)
    time.sleep(1)  # Pausar la ejecución del programa 1 segundo
    num -= 1
