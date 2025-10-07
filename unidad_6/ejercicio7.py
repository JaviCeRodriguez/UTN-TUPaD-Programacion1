"""
Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta-
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
sultados de forma clara.
"""

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
resultado = operaciones_basicas(a, b)
print(f"La suma de {a} y {b} es {resultado[0]}")
print(f"La resta de {a} y {b} es {resultado[1]}")
print(f"La multiplicación de {a} y {b} es {resultado[2]}")
print(f"La división de {a} y {b} es {resultado[3]}")