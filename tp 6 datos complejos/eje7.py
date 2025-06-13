parcial1 = {'Ana', 'Carlos', 'María', 'Pedro', 'Lucía'}
parcial2 = {'Juan', 'María', 'Pedro', 'Sofía', 'Carlos'}

ambos_parciales = parcial1 & parcial2  # Intersección
print(f"Estudiantes que aprobaron ambos parciales: {ambos_parciales}")

solo_parcial1 = parcial1 - parcial2    # Diferencia
solo_parcial2 = parcial2 - parcial1
print(f"Estudiantes que aprobaron solo el Parcial 1: {solo_parcial1}")
print(f"Estudiantes que aprobaron solo el Parcial 2: {solo_parcial2}")

todos_aprobados = parcial1 | parcial2   # Unión
print(f"Todos los estudiantes que aprobaron al menos un parcial: {todos_aprobados}")

input("aprete un botón para finalizar")