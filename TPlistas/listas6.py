#crea una lista con números del 10 al 30 y hacer saltos de 5 en 5
#función range:inicio, fin, paso
numeros_con_saltos = list(range(10, 31, 5))

# mostrar por pantalla los dos príimeros elementos de la lista
primeros_dos_elementos = numeros_con_saltos[0:2]

# Imprimir la lista completa para referencia y los primeros dos elementos.
print(f"La lista completa es: {numeros_con_saltos}")
print(f"Los dos primeros elementos son: {primeros_dos_elementos}")


input("aprete un tecla para continuar")