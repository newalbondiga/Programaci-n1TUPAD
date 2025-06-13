numero = input("Ingrese un número entero: ")


if numero.lstrip('-').isdigit():
    
    if '-' in numero:
        invertido = '-' + numero[:0:-1]  
    else:
        invertido = numero[::-1]
    print(f"Número invertido: {invertido}")
else:
    print("Error: Debe ingresar un número entero válido")

input("pulse una tecla para continuar")