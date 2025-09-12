"""
Ejericico 7:

Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica.
"""

temperaturas = [
    [4, 16],
    [3, 16],
    [5, 14],
    [6, 15],
    [4, 20], # Mayor amplitud acá
    [10, 20],
    [15, 22]
]

# NOTE: Uso None como valor default para posibles errores (que no los hay, pero peco de precavido)
promedios = [None, None] # NOTE: promedios = [min, max]
mayor_amplitud = [None, None] # NOTE: mayor_amplitud = [dia, amplitud]
temps_min = []
temps_max = []

for dia, temp_dia in enumerate(temperaturas):
    temps_min.append(temp_dia[0])
    temps_max.append(temp_dia[1])
    amplitud_term = temp_dia[1] - temp_dia[0]
    
    if mayor_amplitud[1] == None or mayor_amplitud[1] < amplitud_term:
        mayor_amplitud = [dia, amplitud_term]

promedios[0] = sum(temps_min)/len(temps_min)
promedios[1] = sum(temps_max)/len(temps_max)

print('Promedio maximo:', promedios[0])
print('Promedio minimo:', promedios[1])
print(f'Mayor amplitud termica registrada: Dia {mayor_amplitud[0]} (con {mayor_amplitud[1]})')

