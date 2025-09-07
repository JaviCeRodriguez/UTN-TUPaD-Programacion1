"""
Ejercicio 7:

Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""

numero = int(input("Ingrese un numero: "))

suma = 0
for i in range(numero):
    suma += i

print(f"La suma de los numeros comprendidos entre 0 y {numero} es {suma}")