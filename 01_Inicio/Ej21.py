'''
Ejercicio 21:
Crear un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista y muestre por pantalla el
mensaje “Yo estudio <asignatura>”, donde <asignatura> es cada una de las
asignaturas de la lista.
'''

materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in materias:
    print(f"Yo estudio {i}")