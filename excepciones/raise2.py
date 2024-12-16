'''
Al usar raise sin argumentos solo se ejecutará en un bloque except, si intentamos ponerlo fuera de un bloque except
nos dará un error tipo Runtime
'''
def mal_asunto(n):
    try:
        return n/0
    except:
        print("Lo hise")
        raise ValueError

try:
    mal_asunto(0)
except ArithmeticError:
    print("Jaja no, ca pasao?")
    exit(0)
except ValueError:
    print("Valo de erro")
print("Que se ma matao el hijo")