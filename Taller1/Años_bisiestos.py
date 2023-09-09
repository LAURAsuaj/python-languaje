print("Ingrese un año: ")
anno = int(input())

if anno % 4 == 0 and anno % 100 != 0 or anno % 400 == 0 :
    print(anno, "es un año bisiesto.")
else:
    print(anno, "no es un año bisiesto.")
