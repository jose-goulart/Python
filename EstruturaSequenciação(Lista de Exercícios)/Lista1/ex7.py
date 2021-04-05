curupira, boitata, boto, mapinguari, iara = [int (x) for x in input("Digite as porcoes separadas por quebra de linha: ").split()]
totalCurupira = 300 * curupira
totalBoitata = 1500 * boitata
totalBoto = 600 * boto
totalMapinguari = 1000 * mapinguari
totalIara = 150 * iara

total = totalCurupira + totalBoitata + totalBoto + totalMapinguari + totalIara + 225
print(f"Total de mandioca em gramas: {total}")