abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

filtrado = [abecedario[i] for i in range(len(abecedario)) if (i + 1) % 3 != 0]

print("Abecedario completo: ")
print(abecedario)
print("Abecedario sin multiplos de 3:")
print(filtrado)
