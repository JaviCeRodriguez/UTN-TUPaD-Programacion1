"""
Ejercicio 3:

Generar una lista con 15 números enteros al azar entre 1 y 100.
• Crear una lista con los pares y otra con los impares.
• Mostrar cuántos números tiene cada lista.
"""

from random import randint

numeros = []
cantidad = 15
pares = []
impares = []

for _ in range(cantidad):
    numeros.append(randint(1, 100))

for idx in range(len(numeros)):
    numero = numeros[idx]
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print('Lista de numeros: ', numeros)
print(f'Pares ({len(pares)}): ', pares)
print(f'Impares ({len(impares)}): ', impares)