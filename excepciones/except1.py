'''
Las Excepciones se van colocando de la mas concreta, a la mas generica de toda la rama, por eso primero
ponemos la excepcion mas concreta del error y luego la general, asi tiene que ser siempre
'''

try:
    y = 1/0
except ZeroDivisionError:
    print("No se puede dividir por cero")
except ArithmeticError:
    print("Problema Aritmético")
except:
    print("Lain compae....")
print("Como se dices acabé en chino?? Yata...")
