peso = float(input("Introduzca su peso: "))

unidad = input("El peso introducido está en peso o en libras? (K/L): ")

libra = 2.20
if unidad == "K":
    print("Su peso en kilos es de: "+str(peso)+" Kg")
elif unidad == "L":
    libras = float(peso) * libra
    print("Su peso en libras es de: "+str(libras)+" Lb")