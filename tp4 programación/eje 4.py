
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))


inicio = min(num1, num2) + 1  
fin = max(num1, num2)         


suma = sum(range(inicio, fin))


print(f"La suma de los números entre {num1} y {num2} (excluyéndolos) es: {suma}")
input("pulse una tecla para continuar")