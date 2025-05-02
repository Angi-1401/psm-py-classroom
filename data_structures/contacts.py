"""
Escribe un programa que simule una agenda de contactos empleando una lista de diccionarios.
El programa debe permitir al usuario agregar contactos y luego, buscarlos por nombre.
"""

contacts = []

while True:
    action = input("Enter an action (add, search, or exit): ")

    if action == "add":
        name = input("Enter a name: ")
        phone = input("Enter a phone number: ")
        email = input("Enter an email address: ")
        contacts.append({"name": name, "phone": phone, "email": email})

    elif action == "search":
        name = input("Enter a name to search: ")
        for contact in contacts:
            if contact["name"] == name:
                print(contact)
            else:
                print("Contact not found!")

    elif action == "exit":
        break

    else:
        print("Invalid action!")
