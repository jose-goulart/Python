n = int(input("Quantos números da sequência de vc quer que apareça? "))
fib = 1
previousNumber = 0
print("0", end=" - ")
count = 0
if n >= 2:
    while(count < n):
        print(fib, end=" - " if count != (n - 2) else "")
        temp = fib
        fib += previousNumber
        previousNumber = temp
        count +=1