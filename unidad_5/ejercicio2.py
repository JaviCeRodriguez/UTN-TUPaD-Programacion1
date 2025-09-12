"""
Ejercicio 2

Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
"""

productos = []
cantidad = 5

for i in range(cantidad):
    producto = input(f"Ingrese producto ({i + 1}): ")
    productos.append(producto.title())

productos = sorted(productos)
print("Los productos ingresados son:", ', '.join(productos))

prod_a_eliminar = input("Ingrese el producto a eliminar: ").title()
productos.remove(prod_a_eliminar)

print("Los productos ahora son:", ', '.join(productos))