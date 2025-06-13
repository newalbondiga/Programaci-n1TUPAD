
hemisferio = input("¿En qué hemisferio estás? (N para Norte / S para Sur): ").upper()
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día (1-31): "))


if mes < 1 or mes > 12 or dia < 1 or dia > 31:
    print("¡Fecha inválida! Verifica el mes o día ingresado.")
else:
    
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    else:  
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"

    
    if hemisferio == "N":
        estacion = estacion_norte
    elif hemisferio == "S":
        estacion = estacion_sur
    else:
        estacion = "Hemisferio no válido (debe ser N o S)."

    
    print(f"\nEstación actual: {estacion}")
    input("presiona para continuar")