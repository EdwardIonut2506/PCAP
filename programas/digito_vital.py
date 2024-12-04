fecha = input("Ingresa tu fecha de cumpleaños en formato AAAAMMDD: ")

if len(fecha) != 8 or not fecha.isdigit():
    print("Formato de fecha no soportado")
    
else:
    while len() > 1:
        sum = 0
        for c in fecha:
            sum += int(c)
        fecha = str(sum)
    print("Tu numero vital es: " + fecha)