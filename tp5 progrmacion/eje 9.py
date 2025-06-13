def celsius_a_fahrenheit(celsius):
    
    return (celsius * 9/5) + 32

def main():
    print("convierte la temp")
    print("Celsius a Fahrenheit\n")
    
    while True:
        entrada = input("Ingrese temperatura en °C (o 'q' para salir): ").strip()
        
        if entrada.lower() == 'q':
            print("finalizado")
            break
            
        try:
            temp_c = float(entrada)
            temp_f = celsius_a_fahrenheit(temp_c)
            print(f"\n{temp_c}°C = {temp_f:.1f}°F\n")  
        except ValueError:
            print("Debe ingresar un número válido.\n")

if __name__ == "__main__":
    main()
    input("pulsa un tecla para continuar")