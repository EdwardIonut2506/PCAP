p = input("Ingresa la palabra que deseas encontrar: ").upper()
str = input("Ingresa la cadena en donde deseas buscar: ").upper()

contiene= True
posicion = 0

for c in p:
	pos = str.find(c, posicion) 
	if pos < 0:
		contiene = False
		break
	i = pos + 1
if contiene:
	print("Si")
else:
	print("No")
	   