'''
Ejercicio 17:
Crear un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''


print("Tablas de multiplicar")
print("---------------------")

for i in range(1,11):
    print(f"La tabla del {i}")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print("------")

