"""
Escribe un programa que permita agregar tareas a una lista e imprima la lista completa al finalizar.
"""

tasks = []

while True:
    task = str(input("Enter a task (Type 'done' to finish): "))

    if task == "done":
        break
    else:
        tasks.append(task)

print("Tasks:")
for task in tasks:
    index = tasks.index(task)
    print(index + 1, "-", task)
