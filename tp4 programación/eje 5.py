import random

def juego_adivinanza():
    # Generar número aleatorio entre 0 y 9
    numero_secreto = random.randint(0, 9)
    intentos = 0
    
    print("¡Adivina el número secreto entre 0 y 9!")
    
    while True:
        try:
            
            intento = int(input("Tu intento: "))
            intentos += 1
            
            
            if intento == numero_secreto:
                print(f"¡Correcto! El número era {numero_secreto}.")
                print(f"Lo lograste en {intentos} intento{'s' if intentos > 1 else ''}.")
                break
            
            elif intento < numero_secreto:
                print("El número secreto es mayor.")
            else:
                print("El número secreto es menor.")
                
        except ValueError:
            print("Por favor, ingresa solo números enteros entre 0 y 9.")


juego_adivinanza()
input("pulse una tecla para continuar")