lista_numeros = []
valor_ingresado  = ""

print("Ingresar números ordenados. Ingresar '.' para detener.")

# Este while continuará pidiendo entradas al usuario hasta que ingrese "."
while valor_ingresado != ".":
    valor_ingresado  = input()
    # Antes de añadir a la lista, comprobaremos que no es el carácter final "."
    if valor_ingresado != ".":
        # Convertimos el valor ingresado a Double y lo añadimos a la lista
        lista_numeros.append(float(valor_ingresado))

# Obtenemos el tamaño de la lista para saber si la cantidad de números es par o impar
tamano_lista = len(lista_numeros)
if tamano_lista % 2 == 0:
    # Si la cantidad de números es par, se calcula la mediana como el promedio de los dos números en medio
    mediana = (lista_numeros[tamano_lista // 2 - 1] + lista_numeros[tamano_lista // 2]) / 2
    print("La mediana de los números ingresados es: " + str(mediana))
else:
    # Si la cantidad de números es impar, la mediana es el número que se encuentra en el medio de la lista
    mediana = lista_numeros[tamano_lista // 2]
    print("La mediana de los números ingresados es: " + str(mediana))