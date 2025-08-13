"""
Ejercicio 9:

Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
F = 9/5 * C + 32
"""
print("Ejercicio 9:")
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = 9/5 * celsius + 32
print(f"La temperatura en grados Fahrenheit es {fahrenheit}")
