# Ingreso de datos
precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

# Cálculo del monto a pagar
monto_descuento = precio * (descuento / 100)
precio_final = precio - monto_descuento

# Resultado
print(f"El monto del descuento es: {monto_descuento:.2f}")
print(f"El precio final a pagar es: {precio_final:.2f}")