'''Ejercicio 12:
Crear un programa que pida al usuario dos números y muestre por pantalla su división.
Si el divisor es cero, el programa debe devolver un mensaje indicando que no se puede
dividir por 0.'''

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

if num2 == 0 :
    print(f"No se puede dividir por {num2}")
else :
    divi = num1 / num2 
    print(f"La división es {divi}")