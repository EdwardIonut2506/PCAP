n_ganadores = []
print("Introduce los 6 numeros ganadores de la Primitiva:")

for i in range(6):
    while True:
        try:
            n = int(input(f"Introduce el número {i+1}: "))
            if 1 <= n <= 99:
                if n not in n_ganadores:
                    n_ganadores.append(n)
                    break
                else:
                    print("Introduce un número diferente")
            else:
                print("El número debe estar entre 1 y 99")
        except ValueError:
            print("Error, los numeros introducidos no son validos")

n_ganadores.sort()
print("Los numeros ganadores ordenados son: ")
print(n_ganadores)