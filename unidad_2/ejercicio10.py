"""
Utilizando la información aportada en la siguiente tabla sobre las estaciones del año:

Periodo del año (fechas incluidas) y estaciones por hemisferio
- 21 de diciembre a 20 de marzo
  - Hemisferio norte: Invierno
  - Hemisferio sur: Verano
- 21 de marzo a 20 de junio
  - Hemisferio norte: Primavera
  - Hemisferio sur: Otoño
- 21 de junio a 20 de septiembre
  - Hemisferio norte: Verano
  - Hemisferio sur: Invierno
- 21 de septiembre a 20 de diciembre
  - Hemisferio norte: Otoño
  - Hemisferio sur: Primavera

Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S),
qué mes del año es y qué día es. Con esa información el programa deberá imprimir
por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
"""

hemisferio = input("Ingrese en cuál hemisferio se encuentra (N/S): ")
mes = input("Ingrese qué mes del año es: ").lower()
dia = int(input("Ingrese qué día es: "))

if (dia >= 21 and mes == "diciembre") or (mes == "enero" or mes == "febrero") or (dia <= 20 and mes == "marzo"):
    if hemisferio == "N":
        print("Invierno")
    else:
        print("Verano")
elif (dia >= 21 and mes == "marzo") or (mes == "abril" or mes == "mayo") or (dia <= 20 and mes == "junio"):
    if hemisferio == "N":
        print("Primavera")
    else:
        print("Otoño")
elif (dia >= 21 and mes == "junio") or (mes == "julio" or mes == "agosto") or (dia <= 20 and mes == "septiembre"):
    if hemisferio == "N":
        print("Verano")
    else:
        print("Invierno")
else: # (dia >= 21 and mes == "septiembre") or (mes == "octubre" or mes == "noviembre") or (dia <= 20 and mes == "diciembre")
    if hemisferio == "N":
        print("Otoño")
    else:
        print("Primavera")