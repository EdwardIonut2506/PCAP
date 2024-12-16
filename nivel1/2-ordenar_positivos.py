def ordenar(lista):
    positivos_ord = sorted([num for num in lista if num > 0])
    res = []
    indicePos = 0
    
    for num in lista:
        if num > 0:
            res.append(positivos_ord[indicePos])
            indicePos += 1
        else:
            res.append(num)
    return res

lista = [1, -2, 2, 4, 3, -1]
res = ordenar(lista)
print("Lista normal: ", lista)
print(" ")
print("Lista ordenada: ", res)