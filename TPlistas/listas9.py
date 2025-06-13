#lista
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

print("Lista original:", compras)

# a) Agregar jugo a la lista del tercer cliente
compras[2].append("jugo")
print("Después de agregar 'jugo':", compras)

#Reemplazar fideos por tallarine

compras[1][1] = "tallarines"
print("Después de reemplazar 'fideos' por 'tallarines':", compras)

#sacar pan de la lista del primer cliente
compras[0].remove("pan")
print("Después de eliminar 'pan':", compras)

#Imprimir la lista
print("Lista final resultante:", compras)


input("aprete un tecla para continuar")