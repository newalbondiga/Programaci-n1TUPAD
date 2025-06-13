def contar_numeros():
    # Configuración - Cambiar este valor para pruebas (ej: 5 en lugar de 100)
    CANTIDAD_NUMEROS = 100
    
    # Inicializar contadores
    pares = impares = positivos = negativos = cero = 0
    
    print(f"Ingrese {CANTIDAD_NUMEROS} números enteros:")
    
    for i in range(CANTIDAD_NUMEROS):
        while True:
            try:
                num = int(input(f"Número {i+1}: "))
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido. Intente nuevamente.")
        
        
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
        else:
            cero += 1
    
   
    print("\nRESULTADOS:")
    print(f"• Números pares: {pares}")
    print(f"• Números impares: {impares}")
    print(f"• Números positivos: {positivos}")
    print(f"• Números negativos: {negativos}")
    print(f"• Ceros: {cero}")


contar_numeros()


input("pulse una tecla para continuar")