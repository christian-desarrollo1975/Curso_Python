'''
Ejercicio 24:
Crear un programa que almacene el diccionario con los créditos de las asignaturas de
un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los
créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos,
donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus
créditos. Al final debe mostrar también el número total de créditos del curso.
'''

cred_asig = {
    "Matemáticas": 6,
    "Física": 4,
    "Química": 5
}

total_cred = 0

for i, j in cred_asig.items():
    print(f"{i} tiene {j} créditos")
    total_cred += j
print(f"El número total de créditos es {total_cred}")
