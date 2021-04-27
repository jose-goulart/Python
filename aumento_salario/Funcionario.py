class Employee:
    def __init__(self, name, currentSalary):
        self.name = name
        self.currentSalary = currentSalary

    def updateSalary(self):
        if(1500 <= self.currentSalary < 1750):
            newSalary = self.currentSalary + self.currentSalary * 0.12
        elif(1750 <= self.currentSalary < 2000):
            newSalary = self.currentSalary + self.currentSalary * 0.1
        elif(2000 <= self.currentSalary < 3000):
            newSalary = self.currentSalary + self.currentSalary * 0.07
        elif(self.currentSalary > 3000):
            newSalary = self.currentSalary + self.currentSalary * 0.05

        print(f"Nome: {self.name}")
        print(f"Salário Atual: R$ {self.currentSalary}")
        print(f"Salário com Reajuste: R$ {newSalary}")
