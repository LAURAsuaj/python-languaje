numeros = []

for i in range(4):
    numero = int(input("Ingrese el numero: "))
    numeros.append(numero)

n = len(numeros)
for i in range(1, n):
    valor_actual = numeros[i]
    j = i - 1

    while j >= 0 and numeros[j] > valor_actual:
        numeros[j + 1] = numeros[j]
        j -= 1
    numeros[j + 1] = valor_actual

print("Números ordenados:", end=" ")
for num in numeros:
    print(num, end=" ")
