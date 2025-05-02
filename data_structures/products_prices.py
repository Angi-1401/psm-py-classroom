"""
Escribe un programa en el que exista una lista de tuplas con productos y precios.
El programa debe mostrar todos los productos y permitir al usuario consultar el precio de cualquiera de ellos empleando su nombre.
"""

products = [("Bread", 1.99), ("Milk", 0.99), ("Eggs", 0.79), ("Cheese", 2.49)]

# Crear un diccionario con los productos como claves y los precios como valores
catalog = {}
for product, price in products:  # Ver NOTES.md
    catalog[product] = price

print("Products:")
for product, price in products:
    print(product, ":", price)

print("Enter a product name to get its price:")
product_name = input()

if product_name in catalog:
    print("The price of", product_name, "is:", catalog[product_name])
else:
    print("Invalid product name!")
