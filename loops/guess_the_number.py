"""
Escribe un programa que genere un número aleatorio entre 1 y 100 y pida al usuario adivinar el número generado en un total de 5 intentos.
"""

import random  # Librería para generar números aleatorios

number = random.randint(1, 100)  # Generar número aleatorio entre 1 y 100
print("A random number was generated! Now guess it!")

attempts = 0

while attempts < 5:
    guess = int(input("Guess the number: "))

    if guess == number:
        print("You guessed it!")
        break  # Salir del bucle
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

    attempts += 1
    print("You used", attempts, "/ 5 attempts.")

if attempts == 5:
    print("You lost!")
