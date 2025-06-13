
texto = input("Ingresa una frase o palabra: ")


vocales = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')


if texto and texto[-1] in vocales:  #
    texto_modificado = texto + "!"
else:
    texto_modificado = texto


print(texto_modificado)
input("presiona enter para continuar")