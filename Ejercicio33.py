frutas = {"manzana", "banana", "naranja"}

# add(): Agrega un elemento al conjunto
frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}

# remove(): Elimina un elemento (genera error si no existe)
frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

# discard(): Elimina un elemento si está presente (no hace nada si no existe)
frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

# clear(): Elimina todos los elementos del conjunto
frutas.clear()
print(frutas)  # Imprime set()