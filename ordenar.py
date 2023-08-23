print("Ingrese el numero 1 ")
numero1 = float(input())

print("Ingrese el numero 2 ")
numero2 = float(input())

print("Ingrese el numero 3 ")
numero3 = float(input())

print("Ingrese el numero 4 ")
numero4 = float(input())

numeros = [numero1, numero2, numero3, numero4]

numeros.sort()

print("Los números ordenados de menor a mayor son:")
for numero in numeros:
    print(numero)
