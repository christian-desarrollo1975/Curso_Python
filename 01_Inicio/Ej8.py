'''Ejercicio 8:
Crear un programa que pregunte al usuario una cantidad a invertir, el interés anual y el
número de años, y muestre por pantalla el capital obtenido en la inversión.'''
 
 # partimos de la fórmula  C = I * i * t  
 # dónde I --> interes
 # C --> capital
 # i --> interés
 # t --> tiempo

capital = float(input("Ingrese el capital a invertir: "))
int_anual = float(input("Ingrese el interes anual: "))
anios = int(input("Ingrese el número de años: "))

if 0 < int_anual < 1:  # controlar si el interes ya está divido por 100 o no. Caso contrario dividirlo.
    capital_final = capital + capital * int_anual * anios
else:
    int_anual /= 100
    capital_final = capital + capital * int_anual * anios
       
print(f"El capital final obtenido es de {capital_final}" )


# -----------------------------------------------------------------------------
# Otra forma de resolver el control del interes anual para ver si es mayor o no a 1 es

capital = float(input("Ingrese el capital a invertir: "))
int_anual = float(input("Ingrese el interes anual: "))
anios = int(input("Ingrese el número de años: "))

if  int_anual >= 1:
    int_anual /= 100
    
capital_final = capital + capital * int_anual * anios
    
print(f"El capital obtenido en la inversión será {capital_final}")

