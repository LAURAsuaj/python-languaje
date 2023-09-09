caracter = input("Inserte un caracter: ")

if ('A' <= caracter <= 'Z') or ('a' <= caracter <= 'z'):
    if 'A' <= caracter <= 'Z':
        print("Es letra mayúscula")
    else:
        print("Es letra minúscula")
elif '0' <= caracter <= '9':
    print("Es número")
else:
    print("No es letra ni número")
