n = int(input())
i = 0

while(i < n):
    j = 0
    leds = 0
    x = input()
    while(j < len(x)):
        if(x[j] == "1"):
            leds += 2
        elif(x[j] == "7"):
            leds += 3
        elif(x[j] == "4"):
            leds += 4
        elif(x[j] == "2" or x[j] == "3" or x[j] == "5"):
            leds += 5
        elif(x[j] == "6" or x[j] == "9" or x[j] == "0"):
            leds += 6
        else:
            leds += 7
        j+=1
    print(f"{leds} leds")
    i+=1