'''
Ejercicio 20:
Crear un programa que muestre el eco de todo lo que el usuario introduzca hasta que
el usuario escriba “salir” que terminará.
'''

eco = input("Introduzca una pablabra: ")
stop = "salir"

while eco != stop:
    print(f"Ud. escribió {eco}")
    eco = input("Introduzca una pablabra: ")

# Otra lógica con While
while True:
    rta = input("Ingrese una palabra o escriba 'salir' para finalizar")
    if rta == "salir":
        break
    print(rta)
