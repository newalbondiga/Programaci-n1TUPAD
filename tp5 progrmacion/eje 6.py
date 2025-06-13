def mostrar_tabla(numero):
    
    print(f"\nTabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} × {i} = {numero * i}")


if __name__ == "__main__":
    print("Generador de Tablas de Multiplicar")
    print("-----------------------------------")
    
    while True:
        entrada = input("Ingrese un número entero: ")
        
        if entrada.lower() == 'salir':
            print("Programa terminado.")
            break
            
        try:
            numero = int(entrada)
            mostrar_tabla(numero)
        except:
            print("❌ Error: Debes ingresar un número entero válido")
            continue
            input("pulsa un tecla para continuar")