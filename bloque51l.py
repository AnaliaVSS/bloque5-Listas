def encontrar_mayor(num1, num2, num3):
    if num1 == num2 == num3:
        return "Todos los números son iguales."
    elif num1 >= num2 and num1 >= num3:
        return f"El mayor número es: {num1}"
    elif num2 >= num1 and num2 >= num3:
        return f"El mayor número es: {num2}"
    else:
        return f"El mayor número es: {num3}"

# Solicitar al usuario que ingrese tres números enteros
num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))
num3 = int(input("Introduce el tercer número entero: "))

# Determinar y mostrar el mayor número
resultado = encontrar_mayor(num1, num2, num3)
print(resultado)