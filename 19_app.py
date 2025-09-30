# Programa: Conversión de Soles (PEN) a Dólares (USD)

# 1. Solicitar al usuario el monto en soles
monto_soles = float(input("Ingrese el monto en soles (PEN): "))

# 2. Solicitar la tasa de cambio actual (ejemplo: 1 USD = 3.85 PEN)
tasa_cambio = float(input("Ingrese la tasa de cambio actual (1 USD = ? PEN): "))

# 3. Calcular el equivalente en dólares
monto_dolares = monto_soles / tasa_cambio

# 4. Mostrar el resultado con dos decimales
print("\n--- Conversión en Global Change ---")
print(f"Monto en soles: S/ {monto_soles:.2f}")
print(f"Tasa de cambio: 1 USD = S/ {tasa_cambio:.2f}PEN")
print(f"Equivalente en dólares: $ {monto_dolares:.2f}")