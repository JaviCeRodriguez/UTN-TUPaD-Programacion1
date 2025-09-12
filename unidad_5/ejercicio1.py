"""
Ejercicio 1

Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja.
"""

notas = [2, 5, 6, 3, 7, 6.5, 2, 10, 9, 8]

print("Las notas de los estudiantes son: ", notas)

promedio = sum(notas)/len(notas)

print("El promedio de todas las notas es de ", promedio)

print(f"La nota mínima es {min(notas)} y la máxima es {max(notas)}")