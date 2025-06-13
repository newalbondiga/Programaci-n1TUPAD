frase = input("Ingrese una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)


recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1  # Usar 'palabra' en lugar de 'palabras'
    else:
        recuento[palabra] = 1

print("\nResultados:")
print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento: {recuento}")

input("aprete un botón para finalizar")