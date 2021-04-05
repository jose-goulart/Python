def ageAvg(age):
    count = 1
    avg = 0
    while(age >= 0):
        avg += age
        age = int(input())
        if(age >= 0):
            count += 1
    avg = avg / count    
    print(avg, count)

age = int(input())
ageAvg(age)
