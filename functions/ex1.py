def stats(s, b, a, s1, b1, a1):

    sp = (s1 * 100) / s
    bp = (b1 * 100) / b
    ap = (a1 * 100) / a
    print(f"Pontos de saque: {sp}%")
    print(f"Pontos de bloqeio: {bp}%")
    print(f"Pontos de ataque: {ap}%")


i = 1
st = 0
bt = 0
at = 0
st1 = 0
bt1 = 0
at1 = 0
n = int(input("Digite a quantidade de jogadores: "))

while(i <= n):
    name = input("Digite o nome do jogador: ")
    s, b, a = [int(x) for x in input(
        "Digite o total de saques, bloqueios e ataques:").split()]
    st += s
    bt += b
    at += a
    s1, b1, a1 = [int(x) for x in input(
        "Digite o total de saques, bloqueios e ataques com sucesso:").split()]
    st1 += s1
    bt1 += b1
    at1 += a1
    i += 1  
stats(st, bt, at, st1, bt1, at1)
