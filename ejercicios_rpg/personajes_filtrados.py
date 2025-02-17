import random

nom = ["Legolas", "Gandalf", "Gruñón","Frodo", "Sam"]
clases = ["Elfo", "Guerrero", "Enano","Humano","Humano"]

personajes = [
    {"nombre": nombre, "clase": clase, "nivel": random.randint(1, 10)}
    for nombre, clase in zip(nom, clases)
]

for personaje in personajes:
    print(personaje)

personajes_filtrados = list(filter(lambda personaje: personaje['nivel'] >= 5, personajes))
print("Lista de personajes con nivel superior a 5:")
for personaje in personajes_filtrados:
    print(personaje)