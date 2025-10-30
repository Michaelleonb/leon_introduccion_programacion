# Tuplas son inmutables

# Crear una tupla con diversos tipos de elementos
tupla = (4, 20, "Ysabel", 15.75, ["Manzana", "Fresa"], 100)

# Agregar elementos en una tupla (error)
tupla.append(55)
print(tupla)

# Quitar elementos en una tupla (error)
tupla.pop(0)
print(tupla)