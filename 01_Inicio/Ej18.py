'''
Ejercicio 18:
Crear un programa que pida al usuario una palabra y luego muestre por pantalla una a
una las letras de la palabra introducida empezando por la última.
'''

palabra = input("Introduzca una palabra: ")

for letra in palabra[::-1]:  # lo trabajamos con una List y recorremos en orden invertido
    print(letra)

# otra opción es usar
for letra in reversed(palabra):  # lo trabajamos con una List y recorremos en orden invertido
    print(letra)

