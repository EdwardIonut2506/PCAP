import random

nombres_posibles = ["Legolas", "Gandalf", "Gruñón", "Sam", "Frodo", "Gollum"]

def generador_nombres():
    nombres_restantes = nombres_posibles.copy()
    while nombres_restantes:
        nombre = random.choice(nombres_restantes)
        nombres_restantes.remove(nombre)
        yield nombre

generador = generador_nombres()

print("Nombres generados:")
for _ in range(len(nombres_posibles)):
    print(next(generador))
