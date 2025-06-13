numero = input("Ingrese un número entero: ")
if numero.lstrip('-').isdigit():  
    print(f"El número tiene {len(numero.lstrip('-'))} dígitos.")
else:
    print("Error: Debe ingresar un número entero válido.")
 
input("pulse una tecla para continuar")

