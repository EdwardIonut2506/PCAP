'''
Con assert lo que hacemos es manejar excepciones afirmadas, si se ingresa un valor mayor o igual a 0 en este caso...
lo mostrará, pero con assert lo que hacemos es capturar los numero negativos que se introduzcan y se mostrará un error personalizado
'''

import math

x = float(input("Ingresa un número: "))
try:
    assert x >= 0.0
except AssertionError:
    print("HAY QUE SER MAS ASERTIVO >:(")

x = math.sqrt(x)
print(x)