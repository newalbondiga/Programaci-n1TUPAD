stock_productos = {
    'Manzanas': 50,
    'Leche': 30,
    'Pan': 20,
    'Huevos': 40
}

def mostrar_menu():
    print("\n--- GESTIÓN DE STOCK ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a producto existente")
    print("3. Agregar nuevo producto")
    print("4. Mostrar todos los productos")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")
    
    if opcion == '1':
        producto = input("Ingrese el nombre del producto: ")
        if producto in stock_productos:
            print(f"Stock de {producto}: {stock_productos[producto]} unidades")
        else:
            print(f"El producto '{producto}' no existe en el inventario")
    
    elif opcion == '2':
        producto = input("Ingrese el nombre del producto: ")
        if producto in stock_productos:
            try:
                unidades = int(input(f"Ingrese las unidades a agregar a {producto}: "))
                stock_productos[producto] += unidades
                print(f"Stock actualizado: {stock_productos[producto]} unidades")
            except ValueError:
                print("Error: Debe ingresar un número entero")
        else:
            print(f"El producto '{producto}' no existe. Use la opción 3 para agregarlo")
    
    elif opcion == '3':
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto not in stock_productos:
            try:
                unidades = int(input(f"Ingrese el stock inicial de {producto}: "))
                stock_productos[producto] = unidades
                print(f"Producto '{producto}' agregado con {unidades} unidades")
            except ValueError:
                print("Error: Debe ingresar un número entero")
        else:
            print(f"El producto '{producto}' ya existe. Use la opción 2 para agregar unidades")
    
    elif opcion == '4':
        print("\n--- INVENTARIO COMPLETO ---")
        for producto, unidades in stock_productos.items():
            print(f"{producto}: {unidades} unidades")
    
    elif opcion == '5':
        print("Saliendo del sistema de gestión de stock...")
        break
    
    else:
        print("Opción no válida. Por favor ingrese un número del 1 al 5")
        

input("aprete un botón para finalizar")
