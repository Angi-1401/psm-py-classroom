"""
Escribe un programa que pida al usuario ingresar su nombre de usuario y contraseña.
Verifica si coinciden con valores predefinidos.
Si el usuario es correcto pero la contraseña no, muestra "Contraseña incorrecta".
Si ambos son incorrectos, muestra "Acceso denegado".
"""

stored_user = "Tralalero_Tralala_2003"
stored_password = "12345678"

user = str(input("Enter your username: "))
password = str(input("Enter your password: "))

if user == stored_user and password == stored_password:
    print("Access granted!")
elif user == stored_user or password != stored_password:
    print("Password incorrect!")
elif user != stored_user and password == stored_password:
    print("Access denied!")
