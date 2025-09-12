"""
Ejercicio 4:

Dada una lista con valores repetidos:

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

• Crear una nueva lista sin elementos repetidos.
• Mostrar el resultado.
"""

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
nuevos_datos = []

for dato in datos:
    if not (dato in nuevos_datos):
        nuevos_datos.append(dato)

print('Los datos son:', nuevos_datos)