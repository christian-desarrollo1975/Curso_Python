'''Ejercicio 6:
Crear un programa que realice la siguiente operación aritmética [(3+2)/2*5]2. Mostrar el
resultado por pantalla.'''

#print("[(3+2)/2*5]2 =", [(3+2) / 2*5] ** 2)

print(((3+2)/2*5)**2)

# Otra opción es hacer el cálculo y luego imprimirlo
calculo = ((3+2)/2*5)**2
print(f"El resultado de la operación es {calculo}")

# Calculo por término y guardando en variables

suma = (3+2)
division = suma/2
multiplicacion = division*5
potencia = multiplicacion**2
print(f"El resultado de la operación es {potencia}")