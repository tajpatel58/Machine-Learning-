import math

def numberoftriangles(p):
    counter = 0
    for a in range(1,p-1):
        for b in range(a,p-a): # check b in range a to p-a as if b>p-a... then a+b>p
            c = math.sqrt(a**2+b**2)
            if a+b+c==p:
                counter += 1
            else:
                continue
    return counter


MAX=0
MAXp=0
for k in range(12,1000):
    q = numberoftriangles(k)
    if q>MAX:
        MAX=q
        MAXp=k
        print(MAXp)
    else:
        continue
