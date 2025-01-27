frutillas ={"Platanosh":1.35, "Manzanillash":0.80, "Perillash":0.85, "Naranjillash":0.70}

print("***************************")
print("*    1- Platanosh         *")
print("*    2- Manzanillash      *")
print("*    3- Perillash         *")
print("*    4- Naranjillash      *")
print("***************************")
print(" ")

frutash = input("Seleccione su frutilla: ")
try:
    frutash = int(frutash)
except ValueError:
    print("Por favor, ingrese un número válido.")
    exit()

kilillosh = input("Seleccione los kilillosh de la frutilla: ")
try:
    kilillosh = float(kilillosh)
except ValueError:
    print("Por favor, ingrese un valor numérico para los kilogramos.")
    exit()

match frutash:
    case 1:
        res1 = 1.35 * kilillosh
        print("El precio total de losh platanosh compradosh es de: ", res1)
    case 2:
        res2 = 0.80 * kilillosh
        print("El precio total de lash manzanillash compradash es de: ", res2)
    case 3:
        res3 = 0.85 * kilillosh
        print("El precio total de lash perillash compradash es de: ", res3)
    case 4:
        res4 = 0.70 * kilillosh
        print("El precio total de lash naranjillash comrpadash es de: ", res4)
    case _:
        print("Perdona, lash frutillash introducidash no estan en la listilla")
