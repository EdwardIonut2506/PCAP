def read_int(prompt, min, max):
    si = False
    while not si:
        try:
            val = int(input(prompt))
            if si == True:
                si = val >= min and val <= max
            elif not si:
                print("Ingrese un numero valido")
        except ValueError:
            print("Error")
    return val

num = read_int("Ingresa un número: ", -10, 10)
print("El número es:", num)