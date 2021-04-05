def calc():
    i = 0
    positive = 0
    avg = 0
    while(i <= 5):
        age = float(input("Digite a idade: "))
        if(age >= 0):
            positive += 1
            avg += age
        i += 1
    avg = avg / positive

    print(f"{positive} valores positivos\n{avg}")

calc()

