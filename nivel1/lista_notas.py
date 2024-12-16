asignaturas = ["Mates", "Fisica", "Quimica", "Historia", "Lengua"]

aprobadas = []

for asignatura in asignaturas[:]:
    while True:
        try:
            nota = float(input(f"Introduce la nota de {asignatura}: "))
            if 0 <= nota <= 10:
                if nota >= 5:
                    aprobadas.append(asignatura)
                break
            else:
                print("Error, la nota debe estar entre 0 y 10")
        except ValueError:
            print("Por favor, introduce un numero valido")

print("Asignaturas:")
print(asignaturas)

for asignatura in aprobadas:
    if asignatura in asignaturas:
        asignaturas.remove(asignatura)

print("Las asignaturas suspensas son: ")
print(asignaturas)
