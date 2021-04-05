x = int(input("Digite o total percorrido (km): "))
y = round(float(input("Digite o total de combustivel gasto: ")), 1)
avg = round(x / y, 3)
print(f"{avg}km/l")