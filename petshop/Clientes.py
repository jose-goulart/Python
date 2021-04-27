class Customers:
    def __init__(self, breed, furColor, weight, age, dogName, ownerName):
        self.breed = breed
        self.furColor = furColor
        self.weight = weight
        self.age = age
        self.dogName = dogName
        self.ownerName = ownerName


class Vip(Customers):
    def __init__(self, breed, furColor, weight, age, dogName, ownerName, foodRestric, bathFrequency, benefits):
        Customers.__init__(self, breed, furColor, weight,
                           age, dogName, ownerName)
        self.foodRestric = foodRestric
        self.bathFrequency = bathFrequency
        self.benefits = benefits

    def printInfo(self):
        print(f"{self.breed}")
        print(f"{self.furColor}")
        print(f"{self.weight}")
        print(f"{self.age}")
        print(f"{self.dogName}")
        print(f"{self.ownerName}")
        print(f"{self.bathFrequency}")
        print(f"{self.benefits}")

    def foodRestriction(self, foodRestric):
        if(foodRestric.upper() == "S"):
            foodRestric = True
        else:
            foodRestric = False
        return foodRestric

    def oldestDog(self, dogs, n):
        i = 0
        oldestName = ""
        while(i < len(dogs)):
            if(i == 0):
                oldestName = dogs[i]["dogName"]
            elif(dogs[i]["age"] > dogs[i - 1]["age"]):
                oldestName = dogs[i]["dogName"]
            i+=1
        return oldestName
