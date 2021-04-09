gender = input("Digite seu sexo: ").upper()
while(gender != "M" and gender != "F"):
    gender = input("Digite novamente seu sexo: ").upper()
print(f"Seu sexo é {gender}")