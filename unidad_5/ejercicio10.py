"""
Ejercicio 10:

Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana.
"""

ventas = [
    [140, 220, 3040, 4100], # Dia 1
    [40, 20, 150, 590],
    [0, 20, 30, 1],
    [1200, 260, 340, 460],
    [4, 0, 0, 50],
    [10, 2, 0, 4],
]  # ^ Producto 1
productos_nombre = ['Taza de Spiderman', 'Termo Stanley 1L', 'Feastables', 'Alpine A525 de Colapinto']

ventas_producto_por_dia = [[], [], [], []]

for dia in ventas:
    for idx, producto in enumerate(dia):
        ventas_producto_por_dia[idx].append(producto)

print('Total vendido por cada producto:')
for idx, ventas_producto in enumerate(ventas_producto_por_dia):
    print(f'\t{productos_nombre[idx]}: {sum(ventas_producto)}')


mayor_ventas_dia = [None, None] # NOTE: mayor_ventas_dia = [dia, ventas]
for idx, dia in enumerate(ventas):
    total_ventas = sum(dia)
    if mayor_ventas_dia[1] == None or mayor_ventas_dia[1] < total_ventas:
        mayor_ventas_dia = [idx, total_ventas]

print(f'\nDía con mayores ventas totales: {mayor_ventas_dia[0] + 1} (con {mayor_ventas_dia[1]})')


mayor_ventas_producto = [None, None] # NOTE: mayor_ventas_producto = [producto, ventas]
for idx, producto in enumerate(ventas_producto_por_dia):
    total_ventas = sum(producto)
    if mayor_ventas_producto[1] == None or mayor_ventas_producto[1] < total_ventas:
        mayor_ventas_producto = [idx, total_ventas]

print(f'\nProducto más vendido en la semana: {productos_nombre[mayor_ventas_producto[0]]} (con {mayor_ventas_producto[1]})')