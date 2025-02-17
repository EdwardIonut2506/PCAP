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
print("*******************************************")
print("Lista de personajes con nivel superior a 5:")
print("*******************************************")
for personaje in personajes_filtrados:
    print(personaje)

ataques_base = [random.randint(30, 80) for _ in personajes]

ataques_modificados = list(map(lambda ataque: ataque * 1.2 if ataque > 50 else ataque, ataques_base))
print("*************************")
print("Ataque de los personajes:")
print("*************************")
for personaje, ataque in zip(personajes, ataques_modificados):
    print(f"{personaje['nombre']} ({personaje['clase']}) - Nivel {personaje['nivel']} - Ataque Modificado: {ataque:.2f}")
