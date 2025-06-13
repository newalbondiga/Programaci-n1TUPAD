
nombre = input("Ingresa tu nombre: ")


print("\nElige una opción para transformar tu nombre:")
print("1. Mayúsculas (ej: PEDRO)")
print("2. Minúsculas (ej: pedro)")
print("3. Primera letra mayúscula (ej: Pedro)")


opcion = input("\nIngresa el número de la opción deseada (1/2/3): ")


if opcion == "1":
    nombre_transformado = nombre.upper()  
elif opcion == "2":
    nombre_transformado = nombre.lower()  
elif opcion == "3":
    nombre_transformado = nombre.title()  
else:
    nombre_transformado = nombre  
    print("Opción no válida. Se mostrará el nombre sin cambios.")


print("\nResultado:", nombre_transformado)
input("presiona para continuar")

