A, B, C = [float (x) for x in input("Digite 3 valores: ").split()]
triangle = round((A * B) / 2, 3)
circle = round(3.14159 * (C * C), 3)
trapezio = round(((A + B) * C) / 2, 3)
square = round(B * B, 3)
rectangle = round(A * B, 3)

print(f"TRIANGULO: {triangle}")
print(f"CIRCULO: {circle}")
print(f"TRAPEZIO: {trapezio}")
print(f"QUADRADO: {square}")
print(f"RETANGULO: {rectangle}")