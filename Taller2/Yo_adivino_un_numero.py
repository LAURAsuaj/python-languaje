import random

def main():
    random_number = random.randint(1, 100) # Se genera un número aleatorio entre 1 y 100
    print("Adivine el numero.")

    attempt_number = 0

    # Se inicia un bucle infinito para que el usuario continúe adivinando hasta que acierte
    while True:
        attempt_number += 1
        print("Intento " + str(attempt_number) + ":")
        user_guess = int(input())

        # Compara la suposición del usuario con el número aleatorio y le da una pista
        if user_guess < random_number: # Si su suposición es menor, le indica que el número es mayor
            print("Es mayor que " + str(user_guess))
        elif user_guess > random_number: # Si su suposición es mayor, le indica que el número es menor
            print("Es menor que " + str(user_guess))
        else:
            print("Correcto. Adivinaste en " + str(attempt_number) + " intentos.")
            break;

if __name__ == "__main__":
    main()