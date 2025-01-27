nombre = input("Introduzca su nombre: ")
edad = input("Introduzca su edad: ")
direccion = input("Introduzca su direccion: ")
tlf = input("Introduzca su numero de telefono: ")

datos = {"Nombre":nombre, "Edad":edad, "Direccion":direccion, "Telefono":tlf}

print("Hola", datos["Nombre"],"tienes: ",datos["Edad"]," años, vives en: ",datos["Direccion"]," y tu numero de telefono es: ", datos["Telefono"])
