def buscar_codigo(lista, codigo):
    if codigo in lista:
        posicion = lista.index(codigo) + 1
        return f"El código {codigo} se encuentra en la posición {posicion}."
    else:
        return f"El código {codigo} no se ha encontrado."

# Lista de códigos de productos
codigos = ["A123", "B456", "C789", "D012", "E345"]

# Solicitar al usuario que ingrese un código de producto
codigo_ingresado = input("Introduce el código del producto: ")

# Buscar el código en la lista
resultado = buscar_codigo(codigos, codigo_ingresado)
print(resultado)
