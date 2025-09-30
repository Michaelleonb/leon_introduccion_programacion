# Estructura condicional If (si) - elif - else (sino)

# Sintaxis
# if condición:
#   instrucciones a ejecutarse si la condición es verdadera 
# elif condición:
#   instrucciones a ejecutar para la segunda condición
# else:
#   instrucciones a ejecutar si la condición es falsa

# nota 0 - 12.4: desaprobado (condición 1)
# nota 12.5 - 16: Aprobado (condición 2)
# nota 17 - 20: Muy bien, sigue así. (última condición)

nota = 18

if nota <= 12.4:
    print(f"Ud. a desaprobado el curso, su nota es: {nota}")
elif nota <= 16:
    print(f"Ud. a Aprobado el curso, su nota es: {nota}")
else:
    print(f"Muy bien, sigue así. Su nota es: {nota}")