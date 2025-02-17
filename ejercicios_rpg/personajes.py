import random

nom = ["Legolas", "Gandalf", "Gruñón"]
clases = ["Elfo", "Guerrero", "Enano"]

personajes = [
    {"nombre": nombre, "clase": clase, "nivel": random.randint(1, 10)}
    for nombre, clase in zip(nom, clases)
]

for personaje in personajes:
    print(personaje)