#  Ejercicio 03 - funciones

# Convertir de soles a dolares
def convertirMoneda(montoSoles, tipoCambio):
    montoDolares = montoSoles / tipoCambio
    return montoDolares

 # Utilizando la funcion
compraDolares = convertirMoneda(2000, 3.48)
print(f"El monto en dólares es: $ {compraDolares:.2f} dólares")
