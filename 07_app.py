# Conversiones de tipos de datos

# int() -> convierte a número entero
# Sirve para convertir un valor a un número entero (int).
# Si el valor es un número decimal, corta la parte decimal (no redondea).
# Si el valor es un texto que representa un número entero, también funciona.

int("25")     # (cadena a entero)
int(3.9)      # (decimal a entero, elimina los decimales)
int(True)     # (True equivale a 1)
int(False)    # (False equivale a 0)

# float() -> Convierte a número decimal
# Convierte valores a número decimal (float).
# Muy útil para operaciones matemáticas donde necesitas decimales.
float("3.14")   # (cadena a decimal)
float(10)       # (entero a decimal)
float(True)     # 1.0
float(False)    # 0.0

# str() -> Convierte a cadena de texto
# Convierte cualquier tipo de dato a texto (str).
# Útil para mostrar mensajes al usuario o para concatenar textos.
str(100)        # (entero a cadena)
str(3.14)       # "3.14"
str(True)       # "True"
str([1, 2, 3])  # "[1, 2, 3]"

# bool() -> Convierte a valor lógico (True o False)
# Convierte valores a booleano (True o False)
bool(0)       # False
bool(1)       # True
bool("")      # False (cadena vacía)
bool("Hola")  # True (cadena con contenido)
bool([])      # False (lista vacía)
bool([1,2])   # True (lista con elementos)

