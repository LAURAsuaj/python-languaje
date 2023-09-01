print("Ingresa el mensaje cifrado")
mensajeCifrado = input()
print("Número de veces que se movió la letra")
veces = int(input())

mensajeOriginal = ""

for i in range(0, len(mensajeCifrado), 1):
    letra = mensajeCifrado[i]
    minuscula = (letra >= 'a' and letra <= 'z')
    mayuscula = (letra >= 'A' and letra <= 'Z')
    if not(minuscula or mayuscula):
        mensajeOriginal += letra
    else:
        ascii = ord(letra)
        baseAscii = ord('a')
        if mayuscula:
            baseAscii = ord('A')
        nuevoAscii = (ascii - baseAscii - veces) % 26 + baseAscii
        nuevaLetra = chr(nuevoAscii)
        mensajeOriginal += nuevaLetra

print("Mensaje original:", mensajeOriginal)
