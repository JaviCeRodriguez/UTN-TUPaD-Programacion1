"""
Ejercicio 2:

Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""

numero = int(input("Ingrese un numero: ")) # NOTE: Me aseguro que sea entero
cantidad_digitos = len(str(numero))

print(f"El numero {numero} tiene {cantidad_digitos} digitos")