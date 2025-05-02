# Estructuras de Datos en Python

Las estructuras de datos son fundamentales en la programación, ya que permiten organizar y manipular datos de manera eficiente. Python ofrece varias estructuras de datos integradas que son fáciles de usar y muy poderosas. A continuación, se presenta un resumen de las principales estructuras de datos en Python y ejemplos de las funciones más comunes asociadas a cada una.

---

## 1. Listas (`list`)
Las listas son colecciones ordenadas y mutables que permiten almacenar elementos heterogéneos.

### Funciones comunes:
- `append()`: Agrega un elemento al final de la lista.
- `remove()`: Elimina la primera aparición de un elemento.
- `pop()`: Elimina y devuelve el último elemento (o el índice especificado).
- `sort()`: Ordena la lista en su lugar.
- `len()`: Devuelve el número de elementos.

### Ejemplo:
```python
list = [1, 2, 3, 4]
list.append(5)  # [1, 2, 3, 4, 5]
list.remove(2)  # [1, 3, 4, 5]
last = list.pop()  # [1, 3, 4], last = 5
list.sort()  # [1, 3, 4]
```

## 2. Tuplas (`tuple`)
Las tuplas son colecciones ordenadas y inmutables que permiten almacenar elementos heterogéneos.

### Funciones comunes:
- `count()`: Devuelve el número de veces que aparece un elemento en la tupla.
- `index()`: Devuelve el índice de la primera aparición de un elemento en la tupla.

### Ejemplo:
```python
tuple = (1, 2, 3, 4)
count = tuple.count(3)  # 1
index = tuple.index(2)  # 1
```

## 3. Diccionarios (`dict`)
Los diccionarios son colecciones desordenadas y mutables que asocian claves con valores.

### Funciones comunes:
- `get()`: Devuelve el valor asociado a una clave.
- `keys()`: Devuelve una lista de las claves del diccionario.
- `values()`: Devuelve una lista de los valores del diccionario.

### Ejemplo:
```python
dictionary = {'a': 1, 'b': 2, 'c': 3}
value = dictionary.get('b')  # 2
keys = dictionary.keys()  # ['a', 'b', 'c']
values = dictionary.values()  # [1, 2, 3]
```