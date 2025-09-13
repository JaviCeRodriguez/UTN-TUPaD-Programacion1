"""
Ejercicio 8:

Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia.
"""

notas = [
    [2, 3, 4], # Estudiante 1
    [6, 3, 7],
    [7, 3, 8],
    [5, 3, 7],
    [1, 3, 7]
]  # ^ materia 1 

print('Promedios de los estudiantes:')
for idx, estudiante in enumerate(notas):
    print(f"El promedio del estudiante {idx + 1} es {round(sum(estudiante)/len(estudiante), 2)}")

print('\nPromedios de las materias:')
materias = [[], [], []]
for estudiante in notas:
    for idx, materia in enumerate(estudiante):
        materias[idx].append(materia)

for idx, materia in enumerate(materias):
    print(f"El promedio de la materia {idx + 1} es {round(sum(materia)/len(materia), 2)}")