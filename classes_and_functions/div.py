def validate_char(char):
    operators = ["+", "-", "*", "/"]
    if char in operators:
        return True

    return False


def calculator(num_1, num_2, operation):
    try:
        if operation == "+":
            result = num_1 + num_2
        elif operation == "-":
            result = num_1 - num_2
        elif operation == "*":
            result = num_1 * num_2
        else:
            result = num_1 / num_2

        return result
    except:
        return "Estás intentando dividir entre 0 y eso está mal :c"


a = int(input("Ingrese un número: "))
char = input("Introduzca un caracter (+, -, *, /): ")
b = int(input("Ingrese otro número: "))

validate = validate_char(char)
if validate:
    true_result = calculator(a, b, char)
    print(true_result)
else:
    print("Haz ingresado un caracter no soportado por esta pequeña calculadora uwu")
