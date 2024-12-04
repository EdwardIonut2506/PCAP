text = input("Ingresa un mensaje: ")
shift = 0

while shift == 0:
    try:    
        shift = int(input("Ingresa el valor de cambio del cifrado (1..25): "))
        if shift not in range(1,26):
            raise ValueError
    except ValueError:
        print("Error, numero no valido")
        shift = 0

cipher = ''

for char in text:
    if char.isalpha():
        code = ord(char) + shift
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        code -= first
        code %= 26
        cipher += chr(first + code)
    else:
        cipher += char

print(cipher)