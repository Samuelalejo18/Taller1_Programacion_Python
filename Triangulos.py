print("Ingrese el lado a ")
a = float(input())

print("Ingrese el lado b ")
b = float(input())

print("Ingrese el lado c ")
c = float(input())



#if (a > (c + b) && b > (a + c) && c > (b + a)) {
#System.out.print("No es un triángulo válido");
#}
if a == b and b== c:
 print("Triángulo es equilátero")
elif a==b or b==c or a==c:
 print("Triángulo es isósceles")
else:
 print("Triángulo es escaleno")
