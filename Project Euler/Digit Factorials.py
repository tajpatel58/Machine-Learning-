import math

def digitFactorial(a):
    b = list(str(a))
    SUM=0
    for i in range(0,len(b)):
        SUM += math.factorial(int(b[i]))
    if SUM == a:
        return 1 # 1 Indicates rhe number is a DigitFactorial:= THE SUM OF THE FACTORIAL OF IT's DIGITS YIELD THE NUMBER ITSELF
    else:
        return 0

Total=0
for i in range(3,1000000):
    if digitFactorial(i)==1:
        Total+=i
    else:
        continue

print(Total)
