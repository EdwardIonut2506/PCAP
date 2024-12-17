def read_int(prompt, min, max):
    si = False
    while not si:
        try:
            val = int(input(prompt))
            si = True
        except ValueError:
            print("Error")
        if si:
            si = val >= min and val <= max
        elif not si:
            print("El valor no está dentro del rango permitido")
    return val

num = read_int("Ingresa un número: ", -10, 10)
print("El número es:", num)