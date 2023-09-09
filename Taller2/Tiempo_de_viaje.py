import sys

total_minutos = 0
# Iniciamos un bucle infinito para pedir al usuario los minutos de cada tramo del viaje.
while True:
    tramo = int(input("Duracion tramo: "))#  Introduce los minutos de un tramo.

    if tramo == 0: # Comprobamos si el tramo no es un 0
        break
    total_minutos += tramo

horas = total_minutos // 60
minutos = total_minutos % 60

print("Tiempo total de viaje: " + str(horas) + ":" + str(minutos))