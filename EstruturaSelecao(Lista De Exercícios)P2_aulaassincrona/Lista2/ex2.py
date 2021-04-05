# Triplo do maior
#  Escreva um algoritmo que declare duas variáveis de nomes: valor1 e valor2;
# - leia estes valores do teclado (valores inteiros);
# - escreva uma linha na saída, contendo um inteiro, 
# o triplo do maior dos dois valores lidos da entrada. 
# Restrições: 
# A entrada obedece às seguintes restrições: 
# 0 ≤ A ≤ 1000 
# 0 ≤ B ≤ 1000 
# A ≠ B
# Exemplo de saída esperada:
# Valor 1: 10;
# Valor 2: 11;
# Saída : 33

value1, value2 = [int (x) for x in input("Digite dois valores inteiros: ").split()]
if(0 <= value1 <= 1000 and 0 <= value2 <= 1000 and value1 != value2):
    if(value1 > value2):
        triple1 = value1 * 3
        print(triple1)
    else:
        triple2 = value2 * 3
        print(triple2)
else:
    print("Nada a fazer")


