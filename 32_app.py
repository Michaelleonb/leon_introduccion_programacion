# Listas

# Listado de nombres
nombres = ["Juan", "Ana", "Jhon", "Luis", "Juan", "Carlos", "Ana"]

# Obteniendo número de repitencias de elemento
print(nombres.count("Carlos"))
print(nombres.count("Juan"))

# Quitar elementos de lista
nombres.pop(0)
print(nombres)

nombres.pop(3)
print(nombres)

# Ordenar elementos de lista
nombres.sort() # ordena de manera ascendente
print(nombres)

nombres.sort(reverse=True) # ordena de manera descendente
print(nombres)