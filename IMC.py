

print("Ingrese su estatura (en m): ")
estatura = float(input())
print("Ingrese su peso (en kg): ")
peso = float(input())
print("Ingrese su edad: ")
Edad = int(input())  # Convertir Edad a entero

IMC = peso / (estatura * estatura)

if IMC < 22 and Edad < 45:
    print("Su IMC es de " + str(IMC) + " y por su edad de " + str(Edad) + " años, su condición de riesgo es baja")
elif IMC < 22 and Edad >= 45:
    print("Su IMC es de " + str(IMC) + " y por su edad de " + str(Edad) + " años, su condición de riesgo es medio")
elif IMC >= 22 and Edad < 45:
    print("Su IMC es de " + str(IMC) + " y por su edad de " + str(Edad) + " años, su condición de riesgo es medio")
elif IMC >= 22 and Edad >= 45:
    print("Su IMC es de " + str(IMC) + " y por su edad de " + str(Edad) + " años, su condición de riesgo es alto")
