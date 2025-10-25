import random
comenzar = input("Dime tu nombre ").lower()
def juego ():
    Dificultat = int(input("Elije un nivel de dificultat entre 1 y 3: "))
    while Dificultat not in [1, 2, 3]:
        print("Por favor, elije un nivel de dificultat válido entre 1 y 3.")
        Dificultat = int(input("Elije un nivel de dificultat entre 1 y 3: "))
    if Dificultat == 1:
        numero = random.randint(1,25)
        adivinanza = int(input("Adivina un número entre 1 y 25: "))
        while adivinanza != numero:
            if adivinanza < numero:
                print("Demasiado bajo, intenta de nuevo.")
            else:
                print("Demasiado alto, intenta de nuevo.")
            adivinanza = int(input("Adivina un número entre 1 y 25: "))
        print(f"¡Felicidades {comenzar}! Has adivinado el número {numero} correctamente.")
    elif Dificultat == 2:
        numero = random.randint(1,50)
        adivinanza = int(input("Adivina un número entre 1 y 50: "))
        while adivinanza != numero:
            if adivinanza < numero:
                print("Demasiado bajo, intenta de nuevo.")
                
            else:
                print("Demasiado alto, intenta de nuevo.")
            adivinanza = int(input("Adivina un número entre 1 y 50: "))
        print(f"¡Felicidades {comenzar}! Has adivinado el número {numero} correctamente.")
    elif Dificultat == 3:
        numero = random.randint(1,100)
        adivinanza = int(input("Adivina un número entre 1 y 100: "))
        while adivinanza != numero:
            if adivinanza < numero:
                print("Demasiado bajo, intenta de nuevo.")
            else:
                print("Demasiado alto, intenta de nuevo.")
            adivinanza = int(input("Adivina un número entre 1 y 100: "))
        print(f"¡Felicidades {comenzar}! Has adivinado el número {numero} correctamente.")

juego()