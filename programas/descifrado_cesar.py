cif = input("Introduzca el cifrado: ")
txt = " "

for char in cif:
    if not char.isalpha():
        if char == " ":
            txt += " "
        continue
    char = char.upper()
    code = ord(char) -1 
    if code < ord("A"):
        code = ord("Z")
    txt += chr(code)
print(txt)