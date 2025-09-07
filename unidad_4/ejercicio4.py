"""
Ejercicio 4:

Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario
ingrese un 0.
"""

suma = 0

while True:
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        break # NOTE: Si el usuario ingresa un 0, salgo del bucle
    suma += numero

print(f"La suma de los numeros ingresados es {suma}")