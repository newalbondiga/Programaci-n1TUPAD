def calcular_promedio(a, b, c):
    
    return (a + b + c) / 3

def obtener_numero(mensaje):
    
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Debe ingresar un número válido.")

def main():
    print("CALCULADORA DE PROMEDIO")
    print("-----------------------")
    
    
    num1 = obtener_numero("Ingrese el primer número: ")
    num2 = obtener_numero("Ingrese el segundo número: ")
    num3 = obtener_numero("Ingrese el tercer número: ")
    
    
    promedio = calcular_promedio(num1, num2, num3)
    print(f"\nEl promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")

if __name__ == "__main__":
    main()
input("pulsa un tecla para continuar")