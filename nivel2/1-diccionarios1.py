divisa = {"Euro":"€", "Dolar":"$", "Yen":"Y"}

print("*******************")
print("*    1- Euro      *")
print("*    2- Dolar     *")
print("*    3- Yen       *")
print("*******************")
print(" ")
res = input("Seleccione su divisa: ")

match res:
    case "1":
        print("La divisa seleccionada es: ",divisa["Euro"])
    case "2":
        print("La divisa seleccionada es: ",divisa["Dolar"])
    case "3":
        print("La divisa seleccionada es: ",divisa["Yen"])
    case _:
        print("Error, la divisa no está en nuestro sistema :(")


