def saludar_usuario(nombre):
    return f"Hola {nombre}!"


if __name__ == "__main__":
    nombre_usuario = input("Por favor, ingresa tu nombre: ")
    saludo = saludar_usuario(nombre_usuario)
    print(saludo)
    input("pulsa un tecla para continuar")