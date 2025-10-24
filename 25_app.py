def obtenerDatosEmpleado():
    # Recibimos los datos del usuario
    nombre = input("Ingresa el nombre del colaborador: ");
    salarioBruto = input(f"Ingresa el salario bruto de {nombre} en S/. ");
    porcentajeDescuento = input("Ingresa el porcentaje de descuento en % ");

    # Convertir los datos a float para los cálculos
    salarioBrutoValor = float(salarioBruto)
    porcentajeDescuentoValor = float(porcentajeDescuento)
    
    return nombre, salarioBrutoValor, porcentajeDescuentoValor

def imprimirBoleta(nombreEmpleado, salarioBrutoEmpleado, porcentajeDescuentoEmpleado):
    montoDescuento = salarioBrutoEmpleado * (porcentajeDescuentoEmpleado / 100);
    salarioLiquido = salarioBrutoEmpleado - montoDescuento;
    print("--- Boleta de Pago ---");
    print(f"Colaborador: {nombreEmpleado}");
    print(f"Salario Bruto S/. {salarioBrutoEmpleado:.2f}")
    print(f"Monto Descuento S/. {montoDescuento:.2f}")
    print(f"Salario Líquido S/. {salarioLiquido:.2f}")
    print("==================================")

# Flujo del programa
print("Sistema de Generación de Salario 2025")

# Invocamos a la función obtenerDatosEmpleado
nombre, salario, descuento = obtenerDatosEmpleado();

# Generar la impresión de boleta
imprimirBoleta(nombre, salario, descuento)