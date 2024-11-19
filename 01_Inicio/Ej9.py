'''
Ejercicio 9:
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele
hacer venta por correo y la empresa de logística les cobra por el peso de cada paquete
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete
a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Crear un programa que lea
el número de payasos y muñecas vendidos en el último pedido y calcule el peso total
del paquete que será enviado. Mostrar el resultado por pantalla.'''


# Pesos de los juguetes en gramos.
payasos = 112
munneca = 75

num_pay = int(input("Ingrese el número de payasos vendidos: "))
num_munn = int(input("Ingrese el número de muñecas vendidas: "))

peso = (num_pay*payasos) + (num_munn*munneca)

# Opción 1 hace el pasaje a Kilogramos
peso_k = peso / 1000

print("Pedido realizado: ")
print("------------------")
print(f"El paquete va a tener un peso de {peso} gr. Lo que equivale a {peso_k} kilogramos ")

# Opción 2 determina comparando con 1000 para saber si ingreso en gramos o Kilogramos (supongo que 1000
# nunca sería Kilogramos)
if peso >= 1000:
    peso /= 1000
    print(f"El peso del paquete es {peso} kg")
else:
    print(f"El peso del paquete es {peso} g")


