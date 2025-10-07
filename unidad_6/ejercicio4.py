from math import pi

"""
Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
dio como parámetro y devuelva el área del círculo. calcular_peri-
metro_circulo(radio) que reciba el radio como parámetro y devuel-
va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
bas funciones para mostrar los resultados.
"""

def calcular_area_circulo(radio):
    return pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es {calcular_area_circulo(radio)} y el perímetro es {calcular_perimetro_circulo(radio)}")