print("Ingrese el lado a ")
a = float(input())

print("Ingrese el lado b ")
b = float(input())

print("Ingrese el lado c ")
c = float(input())

if a > (c + b) or b > (a + c) or c > (b + a):
 print("No es un triángulo válido")
elif a == b and b== c:
 print("Triángulo es equilátero")
elif a==b or b==c or a==c:
 print("Triángulo es isósceles")
else:
 print("Triángulo es escaleno")
