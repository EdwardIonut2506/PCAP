'''
En este caso vamos a manejar las dos excepciones en la misma linea, con esto evitamos la duplicacion de codigo
este metodo sirve para cuando tenemos excepciones de la misma rama
'''
try:
    y = 1/0
except (ZeroDivisionError, ArithmeticError):
    print("No se puede dividir por cero")
except:
    print("Lain compae....")
print("Como se dices acabé en chino?? Yata...")