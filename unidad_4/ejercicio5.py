"""
Ejercicio 5:

Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""

import random

numero_aleatorio = random.randint(0, 9)

intentos = 0

while True:
    numero = int(input("Ingrese un numero: "))
    intentos += 1
    if numero == numero_aleatorio:
        break # NOTE: Si el usuario adivina el numero, salgo del bucle
    else:
        print("Incorrecto!", end=" ")

print(f"Felicitaciones, adivinaste el numero en {intentos} intentos")