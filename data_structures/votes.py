"""
Escribe un programa que permita ingresar nombres de candidatos en cada iteración (como si fuesen votos) hasta que se decida culminar el proceso de votación.
El programa debe mostrar cuántos votos recibió cada candidato.
"""

votes = {}

while True:
    name = input("Enter a candidate name (Type 'done' to finish): ")

    if name == "done":
        break

    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1

print("Votes:")
for name, votes in votes.items():
    print(name, ":", votes)
