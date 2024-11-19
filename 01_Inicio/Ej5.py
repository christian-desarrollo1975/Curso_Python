
'''
Ejercicio 5:
Crear un programa que pregunte el nombre del usuario y después de que el usuario lo
introduzca muestre por pantalla <NOMBRE> tiene <n> letras.'''

# len(nom_usu)  muestra cantidad de caracteres de la cadena nom_usu   

nom_usu = input ("Ingrese el nombre de usuario: ")
print(nom_usu,"tiene",len(nom_usu),"caracteres" )


nombre = input("Ingrese su nombre: ")
cont = 0  # inicio contador para contar las letras
for letra in nombre:    # recorro desde la primer letra a la última y voy contando en el contador
    cont += 1
print(f"{nombre} tiene {cont} letras")