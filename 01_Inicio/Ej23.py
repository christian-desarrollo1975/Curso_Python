'''
Crear un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio
de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un
mensaje informando de ello.

Fruta Precio (kg)
------------------
Banana 80
Manzana 100
Pera 50
Naranja 70
'''

prec_frutas = {
    "Banana": 80,
    "Manzana": 100,
    "Pera": 50,
    "Naranja": 70
}

# Para convertir la primera letra de una cadena a mayúsculas, utiliza el método capitalize()
# capitalize() devuelve una copia de la cadena con la primera letra en mayúsculas.

fruta = input("Ingrese una fruta: ").capitalize()
kilos = float(input("Ingrese los kilos a comprar: "))

if fruta in prec_frutas:
    precio = kilos * prec_frutas[fruta]
    print(f"Debe abonar {precio}")
else:
    print("La fruta no está en el diccionario.")