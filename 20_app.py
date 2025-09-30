# Datos de entrada
edad = int(input("Ingrese la edad del pasajero: "))

# Determinar tarifa usando condicional 
if edad < 12:
    tarifa = 3.00
    tipo_tarifa = "Tarifa infantil"
elif edad <= 59:
    tarifa = 5.00
    tipo_tarifa = "Tarifa regular"
else:
    tarifa = 2.00
    tipo_tarifa = "Tarifa especial"

# Mostrar tarifa
print("\n-------------------------------------------")
print(f"Ingrese la edad del pasajero: {edad}")
print(f"{tipo_tarifa}: S/ {tarifa:.2f}")
print("-------------------------------------------")
