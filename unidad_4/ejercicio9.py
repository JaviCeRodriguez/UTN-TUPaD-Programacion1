"""
Ejercicio 9:

Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""

iteraciones = 4
suma = 0

for _ in range(iteraciones):
    numero = int(input("Ingrese un numero: "))
    suma += numero

media = suma / iteraciones
print(f"La media de los numeros ingresados es {media}")