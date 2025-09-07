"""
Ejercicio 10:

Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""

numero_invertido = ""
numero = input("Ingrese un numero: ") # NOTE: Asumo que se ingresan digitos

for digito in numero:
    numero_invertido = digito + numero_invertido

print(f"El numero invertido es {numero_invertido}")