
magnitud = float(input("Ingresa la magnitud del terremoto (en escala de Richter): "))


if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    categoria = "Muy fuerte (puede causar daños significativos)"
else:
    categoria = "Extremo (puede causar graves daños a gran escala)"


print(f"Clasificación del terremoto: {categoria}")
input("presiona para continuar")