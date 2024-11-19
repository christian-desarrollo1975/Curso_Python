'''
Ejercicio 15:
Crear un programa para una empresa que tiene salas de juegos para todas las edades
y quiere calcular de forma automática el precio que debe cobrar a sus clientes por
entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de
la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18
años debe pagar 500 y si es mayor de 18 años, 1000.
'''

edad = int(input("Ingrese su edad: "))

if edad < 4:
    print("Ud. no abonará la entrada por ser menor de edad")
elif 4 <= edad < 18:
    print("El costo de su entrada es de $500")
elif edad > 18:
    print("Uds. deberá abonar $1000")
    