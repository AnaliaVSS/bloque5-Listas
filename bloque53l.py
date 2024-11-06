def eliminar_duplicados(lista):
    lista_sin_duplicados = list(set(lista))
    return lista, lista_sin_duplicados

numeros = [1, 2, 2, 3, 3, 3]
original, sin_duplicados = eliminar_duplicados(numeros)
print("Lista original:", original)
print("Lista sin duplicados:", sin_duplicados)
