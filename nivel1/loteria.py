numeros_ganadores = []
print("Introduce los 6 números ganadores de la Lotería Primitiva:")

for i in range(6):
    while True:
        try:
            numero = int(input(f"Introduce el número {i+1}: "))
            if 1 <= numero <= 99:
                if numero not in numeros_ganadores:
                    numeros_ganadores.append(numero)
                    break
                else:
                    print("Introduce un número diferente")
            else:
                print("El número debe estar entre 1 y 99")
        except ValueError:
            print("Error, los numeros introducidos no son validos")

numeros_ganadores.sort()
print("Los números ganadores ordenados de menor a mayor son: ")
print(numeros_ganadores)