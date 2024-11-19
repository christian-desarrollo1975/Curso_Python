'''Ejercicio 11:
Crear un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable.'''

password = "select562"
ver_pass = input("Ingrese la clave: ")

if password == ver_pass :
    print("Felicitaciones la clave es correcta !!!!! ")
else :
    print("La clave introducida NO cohincide")