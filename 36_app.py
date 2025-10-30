# =======================================
# Biblioteca Municipal - Sistema de Inventario
# =======================================

# Lista global para almacenar la colección de libros (lista de diccionarios)
coleccion_libros = []
isbns_registrados = set() # Conjunto para asegurar que los ISBN sean únicos

def validar_input(tipo, mensaje):
    """Función genérica para validar entradas de precio y stock."""
    while True:
        try:
            valor = float(input(mensaje)) if tipo == 'precio' else int(input(mensaje))
            
            if tipo == 'precio':
                if valor > 0:
                    return valor
                else:
                    print("⚠️ Error: El precio de reposición debe ser mayor a 0.")
            elif tipo == 'stock':
                if valor >= 0:
                    return valor
                else:
                    print("⚠️ Error: La cantidad de stock no puede ser negativa.")
            
        except ValueError:
            print(f"❌ Entrada inválida. Por favor, ingrese un número {'decimal' if tipo == 'precio' else 'entero'}.")

def verificar_isbn_unico(isbn):
    """Valida que el código ISBN no se repita."""
    if isbn in isbns_registrados:
        print("❌ Error: El código ISBN ya ha sido registrado. Ingrese uno único.")
        return False
    return True

def ingresar_datos_libros(num_titulos):
    """
    Registra los datos de N títulos de libros, asegurando la unicidad del ISBN.
    Utiliza una tupla para ISBN, título y género durante el ingreso.
    """
    print("\n--- 📖 Registro de Títulos de la Colección ---")
    
    for i in range(1, num_titulos + 1):
        print(f"\nDatos del Título #{i}")
        
        while True:
            isbn = input("Código ISBN (único y alfanumérico): ").strip()
            if verificar_isbn_unico(isbn):
                break
        
        titulo = input("Título del libro: ").strip()
        genero = input("Género (ej: Ficción, Historia, Ciencia, Comedia, romance): ").strip()
        
        # Uso de tupla para almacenar ISBN, título y género (Consideración)
        datos_basicos = (isbn, titulo, genero)
        
        # Validaciones de Precio y Stock
        precio = validar_input('precio', "Precio de reposición (Soles): ")
        stock = validar_input('stock', "Cantidad de copias en stock: ")
        
        # Creación del diccionario del libro
        libro = {
            "isbn": datos_basicos[0],
            "titulo": datos_basicos[1],
            "genero": datos_basicos[2],
            "precio": precio,
            "stock": stock
        }
        
        # Almacenar en la lista global y registrar el ISBN
        coleccion_libros.append(libro)
        isbns_registrados.add(isbn) # Actualiza la variable global

def calcular_valor_total_titulo(precio, stock):
    """Calcula el valor total de un título (precio * stock)."""
    # Variable local para el cálculo
    valor_total = precio * stock
    return valor_total

def generar_reporte_y_estadisticas():
    """Genera el reporte detallado y muestra las estadísticas finales."""
    if not coleccion_libros:
        print("\n--- 📊 Reporte ---")
        print("No hay libros registrados en la colección.")
        return

    valor_total_coleccion = 0.0
    valor_por_genero = {}
    
    libro_mayor_valor = None
    libro_menor_valor = None

    print("\n\n--- 📜 Reporte Detallado de la Colección ---")
    print("-" * 110)
    print(f"| {'ISBN':<15} | {'Título':<30} | {'Género':<15} | {'Precio (S/.)':<13} | {'Stock':<5} | {'Valor Total (S/.)':<17} |")
    print("-" * 110)

    for libro in coleccion_libros:
        # Cálculo del Valor Total del Título
        valor_titulo = calcular_valor_total_titulo(libro["precio"], libro["stock"])
        
        # Acumulación para estadísticas
        valor_total_coleccion += valor_titulo
        
        # Acumular valor por Género
        genero = libro["genero"].lower() # Usar minúsculas para un conteo uniforme
        valor_por_genero[genero] = valor_por_genero.get(genero, 0) + valor_titulo
        
        # Encontrar libro con mayor y menor valor individual
        if libro_mayor_valor is None or valor_titulo > libro_mayor_valor["valor_total"]:
            libro_mayor_valor = {"titulo": libro["titulo"], "valor_total": valor_titulo}
        
        if libro_menor_valor is None or valor_titulo < libro_menor_valor["valor_total"]:
            libro_menor_valor = {"titulo": libro["titulo"], "valor_total": valor_titulo}

        # Mostrar fila del reporte
        print(f"| {libro['isbn']:<15} | {libro['titulo'][:30]:<30} | {libro['genero'][:15]:<15} | {libro['precio']:<13.2f} | {libro['stock']:<5} | {valor_titulo:<17.2f} |")
        
    print("-" * 110)
    
    # Mostrar Estadísticas
    mostrar_estadisticas(valor_total_coleccion, valor_por_genero, libro_mayor_valor, libro_menor_valor)

def mostrar_estadisticas(valor_total_coleccion, valor_por_genero, libro_mayor, libro_menor):
    """Función para mostrar las estadísticas finales."""
    print("\n\n--- 📊 Estadísticas del Inventario ---")
    
    # 1. Valor total de la colección
    print(f"**Valor Total de la Colección:** S/. {valor_total_coleccion:,.2f}")
    
    # 2. Género con mayor valor en inventario
    if valor_por_genero:
        genero_max_valor = max(valor_por_genero, key=valor_por_genero.get)
        valor_max_genero = valor_por_genero[genero_max_valor]
        print(f"**Género con Mayor Valor en Inventario:** {genero_max_valor.capitalize()} (S/. {valor_max_genero:,.2f})")
    
    # 3. El título (libro) con mayor y menor valor individual en inventario
    if libro_mayor:
        print("\n**Título con Mayor Valor Individual:**")
        print(f"  🏆 {libro_mayor['titulo']} (S/. {libro_mayor['valor_total']:,.2f})")

    if libro_menor:
        print("\n**Título con Menor Valor Individual:**")
        print(f"  🔻 {libro_menor['titulo']} (S/. {libro_menor['valor_total']:,.2f})")


def main():
    """Función principal para coordinar el sistema de la biblioteca."""
    print("🌟 Sistema de Gestión de Colección de Libros 🌟")
    
    # Registrar la cantidad total de títulos a ingresar.
    while True:
        try:
            num_titulos = int(input("Ingrese la cantidad total de títulos (libros diferentes) a registrar: "))
            if num_titulos >= 0:
                break
            else:
                print("⚠️ Debe ingresar una cantidad no negativa de títulos.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingrese un número entero.")
            
    if num_titulos > 0:
        # Ingreso de datos de los libros
        ingresar_datos_libros(num_titulos)
    
    # Generar Reporte Final y Estadísticas
    generar_reporte_y_estadisticas()

if __name__ == "__main__":
    main()