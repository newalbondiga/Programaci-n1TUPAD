n = int(input("Ingrese un número entero positivo: "))
if n < 0:
    print("Error: El número debe ser positivo")
else:
    suma = n * (n + 1) // 2
    print(f"La suma de todos los números desde 0 hasta {n} es: {suma}")
input("pulse una tecla para continuar")