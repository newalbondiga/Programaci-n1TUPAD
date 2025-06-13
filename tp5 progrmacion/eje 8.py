def calcular_imc():
    print("\n** Calculadora de IMC **")
    
    
    peso_valido = False
    while not peso_valido:
        peso = input("Ingrese su peso en kg: ")
        if peso.replace('.', '', 1).isdigit() and float(peso) > 0:
            peso = float(peso)
            peso_valido = True
        else:
            print("Ingrese un número positivo.")
    
    
    altura_valida = False
    while not altura_valida:
        altura = input("Ingrese su altura en metros: ")
        if altura.replace('.', '', 1).isdigit() and float(altura) > 0:
            altura = float(altura)
            altura_valida = True
        else:
            print("ingrese un número positivo.")
    
    
    imc = peso / (altura ** 2)
    
    
    print(f"\nSu IMC es: {imc:.2f}")
    
   
    if imc < 18.5:
        print("Clasificación: Bajo peso")
    elif imc < 25:
        print("Clasificación: Peso normal")
    elif imc < 30:
        print("Clasificación: Sobrepeso")
    else:
        print("Clasificación: Obesidad")


calcular_imc()
input("pulsa un tecla para continuar")