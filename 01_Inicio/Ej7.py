'''
Ejercicio 7:
Crear un programa que pida al usuario dos números enteros y muestre por pantalla la
<n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números
introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera
respectivamente.'''


num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese un segundo numero entero: "))


coe=num1/num2
rest=num1%num2
print("La div entre",num1,"y",num2,"da un coeficiente de",coe,"y un resto de",rest)
        
# Otra opción sería
n = int(input("Ingrese un número: ")) # utilizo int para pasar a nro entero
m = int(input("Ingrese otro número: "))
c = n // m
r = n % m

print(f"La división entre {n} y {m} da un cociente {c} y un resto {r}")        
