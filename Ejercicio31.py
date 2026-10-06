persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

# keys(): Devuelve todas las claves
print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])

# values(): Devuelve todos los valores
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])

# items(): Devuelve los pares clave-valor
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])

# update(): Actualiza o añade nuevos pares clave-valor
persona.update({"profesion": "Ingeniero"})
print(persona)           # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}