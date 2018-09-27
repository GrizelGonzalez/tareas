import math

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

if a == 0:
    print("Error: a no debe de ser igual a 0 ")
else:
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    X2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    print(x1, X2)
