'''
Ejercicio 22:
Crear un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre
por pantalla su producto escalar.
'''

vector_1 = [1,2,3]
vector_2 = [-1,0,2]

prod_esc = 0
# len devuelve el nro de elementos de una lista
for i in range(len(vector_1)):
    prod_elemento = vector_1[i] * vector_2[i]
    prod_esc += prod_elemento
    
print(f"El producto escalar de estos vectores es {prod_esc}")
