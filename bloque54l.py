def sumar_listas(lista1, lista2):
    longitud_max = max(len(lista1), len(lista2))
    resultado = []
    
    for i in range(longitud_max):
        valor1 = lista1[i] if i < len(lista1) else 0
        valor2 = lista2[i] if i < len(lista2) else 0
        resultado.append(valor1 + valor2)
    
    return resultado

# Ejemplo de uso
lista1 = [1, 2, 3]
lista2 = [4, 5]
resultado = sumar_listas(lista1, lista2)
print("Resultado de la suma:", resultado)
