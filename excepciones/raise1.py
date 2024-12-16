
def mal_asunto(n):
    raise ZeroDivisionError

try:
    mal_asunto(0)
except ArithmeticError:
    print("Jaja no, ca pasao?")
    exit(0)
print("Que se ma matao el hijo")