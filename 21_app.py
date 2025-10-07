# Datos de entrada (Mes de Setiembre)
vendedores = [
    {"nombre": "Ana", "sueldo_base": 2500, "ventas": 9500},
    {"nombre": "Beto", "sueldo_base": 2200, "ventas": 7800},
    {"nombre": "Carla", "sueldo_base": 2800, "ventas": 12000}
]

# Procesamiento según reglas del negocio
for v in vendedores:
    nombre = v["nombre"]
    sueldo_base = v["sueldo_base"]
    ventas = v["ventas"]

    # Regla 1: Comisión Base (8% de las ventas)
    comision = ventas * 0.08

    # Regla 2: Bono por Rendimiento
    bono = 300 if ventas > 8000 else 0

    # Regla 3: Impuesto a la Renta (8% sobre Comisión + Bono)
    impuesto = (comision + bono) * 0.08

    # Regla 4: Sueldo Final Neto
    sueldo_final = sueldo_base + comision + bono - impuesto

    # Reporte detallado
    print(f"--- Reporte para {nombre} ---")
    print(f"Sueldo Base      : S/ {sueldo_base:.2f}")
    print(f"Ventas del Mes   : S/ {ventas:.2f}")
    print(f"* Comisión (8%)  : S/ {comision:.2f}")
    print(f"* Bono Rendimiento: S/ {bono:.2f}")
    print(f"- Impuesto (8%)  : S/ {impuesto:.2f}")
    print(f"=> Sueldo Final Neto: S/ {sueldo_final:.2f}")
    print("-" * 40)