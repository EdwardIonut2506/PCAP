while True:
    text1 = input("Introduce una palabra: ").upper()
    if not text1.isalpha():
        print("Error: '"+text1+"' no es una cadena alfabetica")
        break
    else:
        text2 = input("Escriba la segunda palabra: ").upper()
        if not text2.isalpha():
            print("Error: '"+text2+"' no es una cadena alfabética")
            break
        
    if sorted(text1) == sorted(text2):
        print("'"+text1+"' y '"+text2+"' son ANAGRAMAS'")
    else:
        print("Las cadenas no son ANAGRAMAS")