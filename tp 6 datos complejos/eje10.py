paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print("Diccionario original (País → Capital):")
for pais, capital in paises_capitales.items():
    print(f"{pais}: {capital}")

print("\nDiccionario invertido (Capital → País):")
for capital, pais in capitales_paises.items():
    print(f"{capital}: {pais}")
    
input("aprete un botón para finalizar")