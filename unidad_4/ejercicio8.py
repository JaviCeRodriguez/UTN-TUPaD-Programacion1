"""
Ejercicio 8:

Escribe un programa que permita al usuario ingresar 100 números enteros.
Luego, el programa debe indicar cuántos de estos números son pares,
cuántos son impares, cuántos son negativos y cuántos son positivos.

(Nota: para probar el programa puedes usar una cantidad menor, pero debe
estar preparado para procesar 100 números con un solo cambio).
"""

pares = 0
impares = 0
negativos = 0
positivos = 0
iteraciones = 4

for _ in range(iteraciones):
    numero = int(input("Ingrese un numero: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero < 0:
        negativos += 1
    else: # NOTE: Asumo que 0 es positivo
        positivos += 1

print(f"Pares: {pares}, Impares: {impares}\nNegativos: {negativos}, Positivos: {positivos}")