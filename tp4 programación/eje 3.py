a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
suma = 0

for num in range(min(a, b) + 1, max(a, b)):
    suma += num

print(f"La suma entre {a} y {b} (excluyéndolos) es: {suma}")
input("pulse una tecla para continuar")