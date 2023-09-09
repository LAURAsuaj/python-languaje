
print("Ingrese el número de juegos ganados por el jugador A: ")
m = int(input())
print("Ingrese el número de juegos ganados por el jugador B: ")
n = int(input())

if abs(m - n) > 2:
    print("Resultado inválido")
elif m == n == 6:
    print("Empate")
elif m >= 6 and m - n >= 2:
    print("El jugador A ganó el set")
elif n >= 6 and n - m >= 2:
    print("El jugador B ganó el set")
else:
    print("El set todavía no termina")

