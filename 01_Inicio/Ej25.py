'''
# Ejercicio 25:
# Crear un programa que, a partir de una lista con todas las letras del abecedario, haga
# un copia y borre de esta última todas las vocales. Luego imprimir por pantalla ambas
# listas, la completa y la sin vocales.
# Para crear la lista del abecedario se puede importar la variable ascii_lowercase del
# módulo string:
'''

#from string import ascii_lowercase
#print(ascii_lowercase)

list_completa = list(ascii_lowercase)
list_completa_copy = list_completa.copy()

for letra in list_completa_copy:
    for vocal in "aeiou":
        if letra == vocal:
            list_completa_copy.remove(letra)
print(list_completa)
print(list_completa_copy)