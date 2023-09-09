
print("Ingrese el número 1")
numero1 = int(input())
print("Ingrese el número 2")
numero2 = int(input())


cociente = numero1/numero2
residuo = numero1 % numero2
print("• La división es ", residuo)

if residuo==0:
    print("• La división es exacta")
else:
    print("• La división no es exacta")
print("Cociente: ",cociente)
print("Residuo: ",residuo)
