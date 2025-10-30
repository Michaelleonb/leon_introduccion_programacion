def validar_puntaje(mensaje):
    """Solicita un puntaje y valida que esté entre 0 y 100."""
    while True:
        try:
            puntaje = int(input(mensaje))
            if 0 <= puntaje <= 100:
                return puntaje
            else:
                print("⚠️ El puntaje debe estar entre 0 y 100.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingrese un número entero.")

def registrar_empleados(num_empleados):
    """Registra los datos de los empleados y sus puntajes de competencias."""
    empleados = []
    print("\n--- Registro de Empleados y Puntajes ---")
    for i in range(1, num_empleados + 1):
        print(f"\nDatos del Empleado #{i}")
        codigo = input("Código (único): ")
        nombre = input("Nombre completo: ")
        departamento = input("Departamento: ")

        # Uso de tupla para almacenar los 4 puntajes de competencias
        puntajes_competencias = (
            validar_puntaje("Puntaje de Calidad de Trabajo (0-100): "),
            validar_puntaje("Puntaje de Productividad (0-100): "),
            validar_puntaje("Puntaje de Comunicación (0-100): "),
            validar_puntaje("Puntaje de Puntualidad (0-100): ")
        )

        empleado = {
            "codigo": codigo,
            "nombre": nombre,
            "departamento": departamento,
            "puntajes": puntajes_competencias,
            "puntaje_ponderado": 0,
            "clasificacion": ""
        }
        empleados.append(empleado)
    return empleados

def calcular_puntaje_ponderado(puntajes):
    """Calcula el puntaje de desempeño ponderado."""
    # Pesos: Calidad: 30%, Productividad: 30%, Comunicación: 20%, Puntualidad: 20%
    pesos = (0.30, 0.30, 0.20, 0.20)
    
    puntaje_ponderado = sum(p * w for p, w in zip(puntajes, pesos))
    # Redondeamos a dos decimales
    return round(puntaje_ponderado, 2)

def clasificar_desempeno(puntaje):
    """Determina la clasificación de desempeño."""
    if puntaje >= 90:
        return "Sobresaliente"
    elif 70 <= puntaje <= 89:
        return "Cumple Expectativas"
    else: # puntaje < 70
        return "Necesita Mejora"

def procesar_evaluacion(empleados):
    """Calcula el puntaje ponderado y la clasificación para todos los empleados."""
    for empleado in empleados:
        puntaje = calcular_puntaje_ponderado(empleado["puntajes"])
        clasificacion = clasificar_desempeno(puntaje)
        
        empleado["puntaje_ponderado"] = puntaje
        empleado["clasificacion"] = clasificacion
    return empleados

def mostrar_reporte(empleados):
    """Muestra el reporte final tabulado de los empleados."""
    print("\n\n--- 📊 Reporte Final de Evaluación de Desempeño ---")
    
    # Encabezado de la tabla
    print("-" * 55)
    print(f"| {'Código':<8} | {'Nombre':<20} | {'Puntaje':<7} | {'Clasificación':<15} |")
    print("-" * 55)
    
    # Filas de la tabla
    for empleado in empleados:
        print(f"| {empleado['codigo']:<8} | {empleado['nombre'][:20]:<20} | {empleado['puntaje_ponderado']:<7.2f} | {empleado['clasificacion']:<15} |")
    
    print("-" * 55)

def mostrar_estadisticas(empleados):
    """Muestra estadísticas clave del proceso de evaluación."""
    print("\n\n--- 📈 Estadísticas del Desempeño ---")
    
    if not empleados:
        print("No hay empleados para mostrar estadísticas.")
        return

    # 1. Total de empleados por cada categoría
    conteo_categorias = {
        "Sobresaliente": 0,
        "Cumple Expectativas": 0,
        "Necesita Mejora": 0
    }
    
    for empleado in empleados:
        conteo_categorias[empleado["clasificacion"]] += 1
        
    print("\nTotal de Empleados por Clasificación:")
    for categoria, total in conteo_categorias.items():
        print(f"- {categoria}: {total}")

    # 2. Empleado con el puntaje más alto y más bajo
    
    # Inicialización con el primer empleado
    mejor_empleado = empleados[0]
    peor_empleado = empleados[0]
    
    for empleado in empleados:
        if empleado["puntaje_ponderado"] > mejor_empleado["puntaje_ponderado"]:
            mejor_empleado = empleado
        if empleado["puntaje_ponderado"] < peor_empleado["puntaje_ponderado"]:
            peor_empleado = empleado

    print("\nEmpleado con el Puntaje Más Alto:")
    print(f"  🏆 {mejor_empleado['nombre']} (Código: {mejor_empleado['codigo']}) con {mejor_empleado['puntaje_ponderado']:.2f} ({mejor_empleado['clasificacion']})")
    
    print("\nEmpleado con el Puntaje Más Bajo:")
    print(f"  🔻 {peor_empleado['nombre']} (Código: {peor_empleado['codigo']}) con {peor_empleado['puntaje_ponderado']:.2f} ({peor_empleado['clasificacion']})")


def main():
    """Función principal para orquestar el proceso de evaluación."""
    print("🌟 Sistema de Evaluación de Desempeño Trimestral 🌟")
    
    # 1. Registrar la cantidad total de empleados a evaluar.
    while True:
        try:
            num_empleados = int(input("Ingrese la cantidad total de empleados a evaluar: "))
            if num_empleados > 0:
                break
            else:
                print("⚠️ Debe ingresar un número positivo de empleados.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingrese un número entero.")
            
    # 2. Registrar datos y puntajes (almacenados en una lista de diccionarios)
    lista_empleados = registrar_empleados(num_empleados)
    
    # 3. Calcular puntaje ponderado y clasificación
    lista_empleados = procesar_evaluacion(lista_empleados)
    
    # 4. Mostrar Reporte Final Tabulado
    mostrar_reporte(lista_empleados)
    
    # 5. Mostrar Estadísticas
    mostrar_estadisticas(lista_empleados)

if __name__ == "__main__":
    main()