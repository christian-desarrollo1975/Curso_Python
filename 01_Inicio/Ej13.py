'''Ejercicio 13:
Crear un programa que pida al usuario un número entero y muestre por pantalla si es
par o impar.'''


# Voy a tomar el resto como verificación para saber si un número es par o no. Eso se hace con % Ejm.(4%2)


# Opción 1 
num = int(input("Ingrese un número: "))
resto = num % 2

if resto == 0 :
    print(f"Su número ingresado es {num} y es PAR")
else :
    print(f"Su número es {num} y es IMPAR")

# opción 2 sería hacer la verificación en el mismo if
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print(f"Su número ingresado es {num} y es PAR")
else :
    print(f"Su número es {num} y es IMPAR")
