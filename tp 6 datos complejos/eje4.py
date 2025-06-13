agenda_telefonica = {}

print("--- Carga de 5 contactos ---")

# Permitir al usuario cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    telefono = input(f"Ingrese el número telefónico de {nombre}: ")
    agenda_telefonica[nombre] = telefono

print("\n--- Consulta de contactos ---")


while True:
    consulta = input("\nIngrese un nombre para buscar (o 'salir' para terminar): ")
    
    if consulta.lower() == 'salir':
        print("¡Hasta luego!")
        break
    
    if consulta in agenda_telefonica:
        print(f"El número de {consulta} es: {agenda_telefonica[consulta]}")
    else:
        print(f"El contacto '{consulta}' no existe en la agenda.")
        
input("aprete un botón para finalizar")
