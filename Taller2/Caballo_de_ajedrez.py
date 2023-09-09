# Tamaño del tablero de ajedrez
TAMANO_TABLERO = 8
SIMBOLO_CABALLO = '♞'

# lista para almacenar posibles movimientos
filas_movimiento = [-2, -1, 1, 2, -2, -1, 1, 2]
columnas_movimiento = [-1, -2, -2, -1, 1, 2, 2, 1]

# Ingresa las coordenadas del caballo
fila = int(input("Ingrese la fila (1-8) donde se encuentra el caballo:\n"))
columna = int(input("Ingrese la columna (1-8) donde se encuentra el caballo:\n"))

# Tablero de ajedrez y ubicación del caballo
tablero = [['*']*TAMANO_TABLERO for _ in range(TAMANO_TABLERO)]
tablero[fila - 1][columna - 1] = SIMBOLO_CABALLO

print("Ubicación actual del caballo:")
for i in range(TAMANO_TABLERO):
    for j in range(TAMANO_TABLERO):
        print(tablero[i][j], end = " ")
    print()

# Posibles movimientos del caballo desde la ubicación actual
print("El caballo puede saltar desde {}-{} a las siguientes posiciones:".format(fila, columna))
for i in range(8):
    nueva_fila = fila + filas_movimiento[i]
    nueva_columna = columna + columnas_movimiento[i]

    # Verificar si el movimiento esta dentro del tablero
    if (nueva_fila >= 1 and nueva_fila <= 8 and nueva_columna >= 1 and nueva_columna <= 8):
        print("{}-{}".format(nueva_fila, nueva_columna))