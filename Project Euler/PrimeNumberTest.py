import math

def primeNumberTest(value):
    t=0
    c = [1]
    for e in range(2,value):
        d = value/e
        if d == math.floor(d):
            t=t+1
            c.append(e)
        else:
            continue
    if t==0:
        print(str(value)+" is a Prime")
        print("Hence it's factors are only:")
        a = [1,value]
        print(a)
    else:
        print(str(value)+" is not a prime")
        print("The factors of "+str(value)+" are:")
        c.append(value)
        print(c)

primeNumberTest(6857)