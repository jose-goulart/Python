# Nome: José Victor Goulart dos Santos
# Matrícula: 20200412
def sequence(lengthS):
    n = 1
    m = 1
    sum = 1
    i = 1
    if(lengthS > 1):
        print("1 1")
        while(i < lengthS):
            n += 1
            m += 2
            div = n / m
            sum += div
            i += 1
            print(n, m)
    else:
        print(n, m)
    print(f"Resultado: {sum}")
lengthS = int(input("Digite o tamanho da série: "))
sequence(lengthS)
