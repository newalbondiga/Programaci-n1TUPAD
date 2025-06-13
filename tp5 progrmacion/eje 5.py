def segundos_a_horas(segundos):
    return segundos / 3600  


if __name__ == "__main__":
    segundos = float(input("Ingresa la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")
    input("pulsa un tecla para continuar")