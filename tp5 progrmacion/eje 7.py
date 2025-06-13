def operaciones_basicas(a, b):
   
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    try:
        division = a / b
    except ZeroDivisionError:
        division = "Indefinido (división por cero)"
    
    return (suma, resta, multiplicacion, division)


if __name__ == "__main__":
    print("Calculadora de Operaciones Básicas")
    print("----------------------------------")
    
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            break
        except ValueError:
            print("Debe ingresar números válidos.\n")

    resultados = operaciones_basicas(num1, num2)
    
    
    print("\nResultados:")
    print(f"Suma: {resultados[0]:.2f}")
    print(f"Resta: {resultados[1]:.2f}")
    print(f"Multiplicación: {resultados[2]:.2f}")
    
    if isinstance(resultados[3], str):
        print(f"División: {resultados[3]}")
    else:
        print(f"División: {resultados[3]:.2f}")
        input("pulsa un tecla para continuar")