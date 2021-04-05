# Faça um programa que leia o ano de nascimento de um jovem
# e informe de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar;
# Se está no momento de se alistar;
# Se passou do tempo do alistamento.
# Seu programa deve também mostrar o tempo que falta ou o que passou do prazo.
# As datas devem ser lidas do teclado (por enquanto não utilizar a função Date)

yearBorned = int(input("Digite seu ano de nascimento: "))
age = 2021 - yearBorned

if(age < 18):
    timeLeft = 18 - age
    print("Ainda vai se alistar")
    print(f"Falta(m) {timeLeft} ano(s) para se alistar")
elif(age == 18):
    print("Esta na hora de se alistar")
else:
    delayedTime = age - 18
    print("Perdeu o prazo para alistamento")
    print(f"Já passou {delayedTime} ano(s) do prazo")
