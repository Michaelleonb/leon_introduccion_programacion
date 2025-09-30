comprobante = "factura"
monto = 150

if comprobante == "factura":
    monto_igv = monto * 0.18
    monto_a_pagar = monto + monto_igv
    print(f"El monto total a pagar con factura es: {monto_a_pagar}")
elif comprobante == "boleta":
    print(f"El monto total a pagar con boleta es: {monto}")
else:
    print("Debe elegir un comprobante válido")