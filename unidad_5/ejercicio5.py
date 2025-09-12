""""
Ejercicio 5:

Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada.
"""

estudiantes = ['Alfa', 'Beta', 'Gamma', 'Theta', 'Epsilon', 'Bombon', 'Burbuja', 'Bellota']

print('Los estudiantes de la comision Z de UTN TUPaD 2025 son:', ', '.join(estudiantes))

operacion = int(input('Queres agregar un nuevo estudiante (1) o eliminar uno existente (2)?: '))

if operacion == 1:
    estudiante = input('Nombre de estudiante nuevo: ')
    estudiantes.append(estudiante)
elif operacion == 2:
    estudiante = input('Nombre de estudiante a eliminar: ')
    if estudiante in estudiantes:
        estudiantes.remove(estudiante)
    else:
        print('No existe el estudiante')
else:
    print('Operacion invalida. Saludos.')

print('Los estudiantes de la comision Z de UTN TUPaD 2025 son:', ', '.join(estudiantes))
