def validImage(x, y, l1, h1, l2, h2):
    if(l1 + l2 <= x and h1 <= y and h2 <= y):
        a = "S"
    elif(l1 + h2 <= x and h1 <= y and l2 <= y):
        a = "S"
    elif(h1 + l2 <= x and l1 <= y and h2 <= y):
        a = "S"
    elif(h1 + h2 <= x and l1 <= y and l2 <= y):
        a = "S"
    else:
        a = "N"
    return a
x, y = [int(x) for x in input(
        "Digite a L e H da pagina do album: ").split()]
l1, h1 = [int(x) for x in input(
        "Digite a L e H da pagina da foto: ").split()]
l2, h2 = [int(x) for x in input(
        "Digite a L e H da pagina da foto: ").split()]
print(validImage(x, y, l1, h1, l2, h2))