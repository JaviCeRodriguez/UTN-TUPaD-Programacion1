"""
Ejercicio 4:

Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro.
"""
print("Ejercicio 4:")
pi = 3.14
radio = float(input("Ingrese el radio del círculo: "))
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(f"El área del círculo es {area} y el perímetro es {perimetro}")
