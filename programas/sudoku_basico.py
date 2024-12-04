sudokuOk= False
tablero = []
for i in range(9):
    fila = input(f"Introduce un numero(Linea {i + 1} ):")
    if fila.isnumeric() and len(fila) == 9:
        if sorted(fila) != list("123456789"):
            print(sorted(fila))
            print("La fila debe contener el intervalo del 1 al 9")
            break
        else:
            sudokuOk = True
            tablero.append(fila)

if sudokuOk:
    print("El sudoku es valido")
else:
    print("El sudoku no es valido")