def calcular_media():
    
    CANTIDAD_NUMEROS = 100  
    
    suma = 0
    numeros = []
    
    print(f"Ingrese {CANTIDAD_NUMEROS} números enteros:")
    
    for i in range(CANTIDAD_NUMEROS):
        while True:
            try:
                num = int(input(f"Número {i+1}/{CANTIDAD_NUMEROS}: "))
                suma += num
                numeros.append(num)
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido. Intente nuevamente.")
    
    media = suma / CANTIDAD_NUMEROS
    print(f"\nLa media de los {CANTIDAD_NUMEROS} números es: {media:.2f}")


calcular_media()

input("pulse una tecla para continuar")