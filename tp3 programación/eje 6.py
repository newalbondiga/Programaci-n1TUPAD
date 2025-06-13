import random
from statistics import mean, median, mode


numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]


media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
try:
    moda = mode(numeros_aleatorios)
except StatisticsError:
    moda = "No hay moda única"  


if media > mediana and mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana and mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
elif media == mediana == moda:
    sesgo = "Sin sesgo (distribución simétrica)"
else:
    sesgo = "No se puede determinar claramente el sesgo"


print("Lista generada:", numeros_aleatorios)
print("\n--- Resultados Estadísticos ---")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print("\n--- Tipo de Sesgo ---")
print(sesgo)