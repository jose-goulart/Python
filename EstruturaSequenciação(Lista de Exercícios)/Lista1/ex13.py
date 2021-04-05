height, width = [int (x) for x in input("Digite a altura e a largura (m): ").split()]
area = height * width
inkNeeded = area / 2
print(f"Area da parede: {area}m² Tinta necessaria: {inkNeeded}Litro(s)")