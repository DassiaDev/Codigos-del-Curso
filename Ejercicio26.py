frutas = ["manzana", "banana", "naranja"]

# append(): Agrega un elemento al final
frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]

# insert(): Inserta un elemento en una posición específica
frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]

# remove(): Elimina la primera aparición de un elemento
frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]

# pop(): Elimina y devuelve el elemento en una posición específica
fruta_eliminada = frutas.pop(2)
print(frutas)         # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"

# sort(): Ordena los elementos en orden ascendente
frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]

# reverse(): Invierte el orden de los elementos
frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]