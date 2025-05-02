"""
Escribe un programa que simule una partida de Piedra, Papel o Tijeras entre dos jugadores.
El programa pide a dos jugadores que ingresen su elección y luego determina quién gana.
"""

print("Rock, Paper o Scissors!")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

player_1 = input("Player 1, choose rock, paper or scissors (1, 2, 3): ")
player_2 = input("Player 2, choose rock, paper or scissors (1, 2, 3): ")

if player_1 == player_2:
    print("It's a tie!")
elif (
    (player_1 == "1" and player_2 == "3")
    or (player_1 == "2" and player_2 == "1")
    or (player_1 == "3" and player_2 == "2")
):
    print("Player 1 wins!")
elif (
    (player_2 == "1" and player_1 == "3")
    or (player_2 == "2" and player_1 == "1")
    or (player_2 == "3" and player_1 == "2")
):
    print("Player 2 wins!")
else:
    print("Invalid input!")
