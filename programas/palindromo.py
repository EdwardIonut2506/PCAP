text = input("Ingresa un texto: ")
text = text.replace(' ','')

if len(text) > 1 and text.upper() == text[::-1].upper():
	print("Es un palíndromo")
else:
	print("No es un palíndromo")
