# Programa: Cálculo automático de tarifas para MoviExpress

# 1. Solicitar la edad del pasajero
edad = int(input("Ingrese la edad del pasajero: "))

# 2. Determinar la tarifa usando condicional if - elif - else
if edad < 12:
    tarifa = 3.00
    tipo_tarifa = "Tarifa infantil"
elif edad <= 59:
    tarifa = 5.00
    tipo_tarifa = "Tarifa regular"
else:
    tarifa = 2.00
    tipo_tarifa = "Tarifa especial"

# 3. Mostrar el resultado formateado
print("\n-------------------------------------------")
print(f"Ingrese la edad del pasajero: {edad}")
print(f"{tipo_tarifa}: S/ {tarifa:.2f}")
print("-------------------------------------------")