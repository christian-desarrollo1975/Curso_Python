'''
Ejercicio 19:
Crear un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase.
'''

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

contador = 0
for i in frase:
    if letra == i:
        contador =+ 1
if contador == 1: # lo utilizo para poder escribir correctamente la frase que se muestra por pantalla
    print(f"La letra {letra} apareció {contador} vez en la frase ingresada")
else:
    print(f"La letra {letra} apareció {contador} veces en la frase ingresada")


# Opción sencilla utilizando una función para count que permite contar 
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
contador = frase.count(letra) # función count
if contador == 1: # lo utilizo para poder escribir correctamente la frase que se muestra por pantalla
    print(f"La letra {letra} apareció {contador} vez en la frase ingresada")
else:
    print(f"La letra {letra} apareció {contador} veces en la frase ingresada")
