'''Ejercicio 4:
Crear un programa que pregunte el nombre del usuario y un número entero e imprima por pantalla en líneas
distintas el nombre del usuario tantas veces como el número introducido. '''

nom_usu = input("Ingrese su nombre de usuario: ")
num_ent = int(input("Ingrese un nomero entero: "))
while num_ent > 0:
    print(num_ent,"",nom_usu) # agregué la impresión de num_ent para enumerar la cantidad de impresiones para casos largos
    num_ent -= 1

# Otra alternativa es usando la función range() 
# retorna una sucesión de números enteros. Cuando se le pasa un único argumento n,  la sucesión empieza 
# desde el cero y culmina en n-1.

nom_usu = input("Ingrese su nombre de usuario: ")
num_ent = int(input("Ingrese un nomero entero: "))
for i in range(num_ent):
    print(nom_usu)


# usando únicamente print podemos hacer así

nom_usu = input("Ingrese su nombre de usuario: ")
num_ent = int(input("Ingrese un nomero entero: "))
print(f"{nom_usu}\n" * num_ent)

# Opciones de print \n baja el renglón 
print(f"{nom_usu}\n" * 5)


