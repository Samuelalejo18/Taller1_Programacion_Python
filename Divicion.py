print("Ingrese el numerador ")
numerador = float(input())

print("Ingrese el denominador: ")
denominador = float(input())
division = numerador / denominador
modulo = numerador % denominador

if denominador == 0:
    print("Error matemático, no es posible dividir entre 0")

elif modulo == 0:
    print("Es una división exacta.")
else:
    print("No es una división exacta.")
    print("El residuo es", modulo)

print("El cociente es:", division)
