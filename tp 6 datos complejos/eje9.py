agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("lunes", "14:30"): "Almuerzo con cliente",
    ("martes", "09:00"): "Clase de programación",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "11:00"): "Revisión de proyectos"
}

def consultar_agenda():
    print("\n--- CONSULTAR AGENDA ---")
    dia = input("Ingrese el día (ej: lunes, martes): ").lower()
    hora = input("Ingrese la hora en formato HH:MM (ej: 10:00): ")
    
    clave_consulta = (dia, hora)
    
    if clave_consulta in agenda:
        print(f"\nEvento programado: {agenda[clave_consulta]}")
    else:
        print("\nNo hay eventos programados para ese día y hora")

def agregar_evento():
    print("\n--- AGREGAR EVENTO ---")
    dia = input("Ingrese el día (ej: lunes, martes): ").lower()
    hora = input("Ingrese la hora en formato HH:MM (ej: 10:00): ")
    evento = input("Ingrese la descripción del evento: ")
    
    agenda[(dia, hora)] = evento
    print(f"\nEvento '{evento}' agregado correctamente para el {dia} a las {hora}")

def mostrar_menu():
    print("\n--- AGENDA DE EVENTOS ---")
    print("1. Consultar evento")
    print("2. Agregar nuevo evento")
    print("3. Mostrar agenda completa")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        consultar_agenda()
    elif opcion == '2':
        agregar_evento()
    elif opcion == '3':
        print("\n--- AGENDA COMPLETA ---")
        for (dia, hora), evento in agenda.items():
            print(f"{dia.capitalize()} {hora}: {evento}")
    elif opcion == '4':
        print("Saliendo de la agenda...")
        break
    else:
        print("Opción no válida. Por favor ingrese 1, 2, 3 o 4")
        
input("aprete un botón para finalizar")       
