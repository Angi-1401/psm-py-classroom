# Notas interesantes

## Desempaquetado en Python con listas de tuplas

En el archivo `products_prices.py`, se utiliza un bucle `for` con dos variables para iterar sobre una lista de tuplas. A continuación, se explica cómo funciona este mecanismo de manera sencilla.

### Código relevante

```python
for product, price in products:
    catalog[product] = price
```

### Explicación

1. **Lista de tuplas**: En el programa, la variable `products` es una lista que contiene tuplas. Cada tupla tiene dos valores: el nombre del producto y su precio. Por ejemplo:

```python
products = [("Bread", 1.99), ("Milk", 0.99), ("Eggs", 0.79), ("Cheese", 2.49)]
```

2. **Iteración con dos variables:** Cuando Python recorre la lista con `for product, price in products:`, en cada iteración toma una tupla de la lista, como `("Bread", 1.99)`.

3. **Desempaquetado automático:** Python separa automáticamente los valores de la tupla:

   - El primer valor `("Bread")` se asigna a la variable `product`.
   - El segundo valor `(1.99)` se asigna a la variable `price`.

4. **Uso de las variables:** Dentro del bucle, puedes usar product y price directamente para trabajar con el nombre del producto y su precio. Por ejemplo:

```python
for product, price in products:
    print(product, "costs", price)
```
La misma lógica puede ser aplicada a otras tareas de programación, como imprimir valores de listas de tuplas.
Este mecanismo hace que el código sea más legible y fácil de trabajar cuando se manejan estructuras de datos como listas de tuplas.
