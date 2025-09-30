# datos de entrada
monto = float (input(" Ingrese el monto en soles (PEN): "))
tasa = float (input("Ingrese la tasa de cambio actual (1 USD = ? PEN): "))

# calcular cambio 
cambio = monto/tasa

#mostrar datos calculados

print ("\n---Conversión en Global Change---")

#mostrar "2.f" con dos decimales
print (f"Monto en soles: S/.{monto:.2f}")
print (f"Tasa de cambio: 1 USD = S/.{tasa:.2f}")
print (f"Equivalente en dólares: ${cambio:.2f}")

