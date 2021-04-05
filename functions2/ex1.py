def changeSalary(a):
    if(s <= 400):
        p = 15
    elif(400.01 <= s <= 800):
        p = 12
    elif(800.01 <= s <= 1200):
        p = 10
    elif(1200.01 <= s <= 2000):
        p = 7
    else:
        p = 4
        
    p = p / 100
    increased = s * p
    p = p * 100
    newS = s + increased
    print(
        f"Novo salario: {newS}\nReajuste ganho: {increased}\nEm percentual: {p}")

s = float(input("Digite o salario: "))
changeSalary(s)
