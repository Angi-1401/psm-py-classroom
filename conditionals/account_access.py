"""
Escribe un programa que pregunte la edad del usuario y si tiene una cuenta registrada. En caso afirmativo, permitir el acceso solo si el usuario tiene al menos 18 años y está registrado.
"""

choose = input("Do you have an account? (y/n): ")

if choose == "y" or choose == "Y":
    age = int(input("Enter your age: "))

    if age >= 18:
        print("Access granted!")
    else:
        print("Access denied.")
else:
    print("You need an account, but I won't let you to create one!")
