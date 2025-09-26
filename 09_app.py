# Cálculo de monto a pagar para una factura (IGV - 18%)

# Definir el subtotal
subtotal = float(input("Ingresa el subtotal: "))

# Definir el cálculo
monto_igv = subtotal * 0.18
monto_pagar = subtotal + monto_igv

# Imprimir resultados
print(f"Monto de subtotal: {subtotal}")
print(f"Monto de IGV 18%: {monto_igv}")
print(f"Monto total a Pagar: {monto_pagar}")