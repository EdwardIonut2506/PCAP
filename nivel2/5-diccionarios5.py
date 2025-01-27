curso ={"Mates":6, "Fisica":4, "Quimica":5}
total = 0

for asignatura, creditos in curso.items():
    print(asignatura, " tiene ", creditos, " creditos")
    total += creditos
print("Numero total de creditos del curso :", total)