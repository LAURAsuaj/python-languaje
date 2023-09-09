positivo = 0
negativo = 0

print("Ingrese varios valores, termine con cero:")

while True:
    num = int(input())

    # Si el número es cero, terminamos la entrada
    if (num == 0):
        break

    if num > 0:
        # positivos, si el número es mayor a cero
        positivo += 1
    elif num < 0:
        # negativos, si el número es menor a cero
        negativo += 1

# Imprimir el histograma para los números positivos
print("Positivos: ", "*" * positivo)

# Imprimir el histograma para los números negativos
print("Negativos: ", "*" * negativo)