import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


if __name__ == "__main__":
    radio = float(input("Ingresa el radio del círculo: "))
    
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    
    print(f"Área del círculo: {area:.2f}")  
    print(f"Perímetro del círculo: {perimetro:.2f}")
    input("pulsa un tecla para continuar")