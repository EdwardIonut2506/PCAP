line  = input("Ingresa una linea de numeros, separalos con espacios: ")
strings = line.split()

total = 0

try:
    for substr in strings:
        total += float(substr)
    print("El total es: ", total)
except:
    print("Error, ", substr, " son numeros")
