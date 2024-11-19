'''Ejercicio 14:
En una determinada empresa, sus empleados son evaluados al final de cada año. Los
puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir
los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las
cifras mencionadas. A continuación se muestra una tabla con los niveles
correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel
es de 100000 multiplicada por la puntuación del nivel.

Nivel Puntuación
Inaceptable 0.0
Aceptable 0.4
Meritorio 0.6 o más

Crear un programa que lea la puntuación del usuario e indique su nivel de rendimiento,
así como la cantidad de dinero que recibirá el usuario.'''

inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
coef = 100000
puntuacion = float(input("Ingrese la puntuación: ")) #por el tipo de datos definido determino que sea float

while True:
    if puntuacion == inaceptable:
        print(f"Su puntuación es {puntuacion} y es Inaceptable")
        print("La cantidad de dinero a percibir es", puntuacion * coef)
        break
    elif puntuacion == aceptable:
        print(f"Su puntuación es {puntuacion} y es Aceptable")
        print("La cantidad de dinero a percibir es", puntuacion * coef)
        break
    elif puntuacion >= meritorio:
        print(f"Su puntuación es {puntuacion} y es Meritorio")
        print("La cantidad de dinero a percibir es", puntuacion * coef)
        break
    else: # utilizo esta opción para los casos que no cumplan con el ingreso de la puntuación correcta
        print(f"La puntuación {puntuacion} no es válida")
        puntuacion = float(input("Ingrese la puntuación nuevamente: "))