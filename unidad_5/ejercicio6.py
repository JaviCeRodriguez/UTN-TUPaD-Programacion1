"""
Ejercicio 6:

Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero).
"""

numeros = [1, 2, 3, 4, 5, 6, 7]
nuevos_numeros = []
rotacion_cantidad = -1

for idx in range(rotacion_cantidad, len(numeros) + rotacion_cantidad):
   nuevos_numeros.append(numeros[idx])

print('Lista antes:', numeros)
print('Lista despues:', nuevos_numeros)


"""
Con slicing + concatenacion
nuevos_numeros = numeros[rotacion_cantidad:] + numeros[0:len(numeros) + rotacion_cantidad]
"""